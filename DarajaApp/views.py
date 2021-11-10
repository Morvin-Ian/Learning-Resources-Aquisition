from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

import requests
import json

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .access_tkn_generator import generate_access_token
from .credentials import bs_shortcode,lnm_passkey
from .timestamp import format_time
from  .password_generator import decode_password

from .models import TransactionDetails


def updatephone(request,id):
    phone_user = User.objects.get(id=id)
    if request.method == 'POST':
        phone = request.POST['phone']
        if phone_user.transactiondetails_set.all():
            for amount in phone_user.transactiondetails_set.all():
                latest_amount=amount.amount
            sent_amount = str(latest_amount)
            
            if len(phone) == 12 and phone.startswith("2547"):
                phone_user.transactiondetails_set.create(user=phone_user, phone=phone, amount=sent_amount)
                return redirect('home-page')
            else:
                messages.info(request, f"the phone number {phone} not a valid kenyan number/has a wrong format")

        else:
            if len(phone) == 12 and phone.startswith("2547"):
                phone_user.transactiondetails_set.create(user=phone_user, phone=phone, amount=1)
                return redirect('home-page')
            else:
                messages.info(request, f"the phone number {phone} not a valid kenyan number/has a wrong format")

    return render(request, 'DarajaApp/phone.html',{"phone_user":phone_user})



class MpesaApiView(APIView):    
    def get(self, request,id):
        payer = User.objects.get(id=id)

        for pay in payer.transactiondetails_set.all():
            amount = pay.amount
            phone = pay.phone
        

        sent_amount= str(amount)
        sent_number = str(phone)
        print(sent_amount)
        access_token = generate_access_token()
        api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {"Authorization": "Bearer %s" %access_token }


        request = {    
            "BusinessShortCode":bs_shortcode,    
            "Password":decode_password(),    
            "Timestamp":format_time(),    
            "TransactionType": "CustomerPayBillOnline",    
            "Amount":sent_amount,    
            "PartyA":sent_number,    
            "PartyB":bs_shortcode,    
            "PhoneNumber":sent_number,    
            "CallBackURL":"https://essaybees.com/home",    
            "AccountReference":"Rongo University",    
            "TransactionDesc":"Pay library penalties"
        }

        response = requests.post(api_url, json=request, headers=headers) #The response can either be a succesful transaction or a failed transaction 
        response_string =response.text
        res = json.loads(response_string)

        merchant_id = res['MerchantRequestID']
        checkout_id = res['CheckoutRequestID']
        code = res['ResponseCode']
        response_des = res['ResponseDescription']

        json_format = {

        'MerchantRequestId': merchant_id,
        'CheckoutRequestId': checkout_id,
        'ResponseCode':code, 
        'ResponseDescription':response_des

        }
        
        return Response(json_format) #Check the reponse in your teminal

