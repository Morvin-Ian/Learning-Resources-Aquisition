from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse,HttpResponse

import requests
import json

from .access_tkn_generator import generate_access_token
from .credentials import bs_shortcode,lnm_passkey
from .timestamp import format_time
from  .password_generator import decode_password


from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import TransactionDetails
from .models import LNMOnline
from .serializers import LNMOnlineSerializer






class LNM(APIView):
    def mpesa_payments(self, amount: str, phone: str) -> dict:
        access_token = generate_access_token()
        api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {"Authorization": "Bearer %s" %access_token }
        request = {    
                    "BusinessShortCode":bs_shortcode,    
                    "Password":decode_password(),    
                    "Timestamp":format_time(),    
                    "TransactionType": "CustomerPayBillOnline",    
                    "Amount":amount,    
                    "PartyA":phone,    
                    "PartyB":bs_shortcode,    
                    "PhoneNumber":phone,  
                    "CallBackURL": "https://rulibrary.herokuapp.com/api/lnm",
                    "AccountReference":"Rongo University",    
                    "TransactionDesc":"Pay library penalties"
                }
        response = requests.post(api_url, json=request, headers=headers) #The response can either be a succesful transaction or a failed transaction 
        response_string =response.text
        res = json.loads(response_string)

        res_code = res['ResponseCode']
        if(res_code == '0'):
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

            transaction= MpesaCallBack.objects.create(
                merchant_request_id = merchant_request_id,
                checkout_request_id = checkout_request_id,
                response_code = response_code,
                response_description = response_description,
            )

            transaction.save()  
            return json_format
    
    def post(self, request, *args, **kwargs):
        payment_res = self.mpesa_payments(amount="1", phone="245726486929")
        return  HttpResponse("Done")

    

def updatephone(request,id):
    phone_user = User.objects.get(id=id)
    if request.method == 'POST':
        phone = request.POST['phone']
        
        if phone_user.transactiondetails_set.all():
            for amount in phone_user.transactiondetails_set.all():
                latest_amount=+amount.amount
            sent_amount = str(latest_amount)
            print(sent_amount)
                
            if len(phone) == 12 and phone.startswith("2547"):
                access_token = generate_access_token()
                api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
                headers = {"Authorization": "Bearer %s" %access_token }
                request = {    
                            "BusinessShortCode":bs_shortcode,    
                            "Password":decode_password(),    
                            "Timestamp":format_time(),    
                            "TransactionType": "CustomerPayBillOnline",    
                            "Amount":sent_amount,    
                            "PartyA":phone,    
                            "PartyB":bs_shortcode,    
                            "PhoneNumber":phone,    
                            "CallBackURL": "https://rulibrary.herokuapp.com/api/lnm",
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
                print(json_format)
                return redirect('home-page')
                
            else:
                messages.info(request, f"the Phone Number '{phone}' not valid or Wrong format")
        else:
            messages.info(request, f"No charges for {phone_user.username} ")
    return render(request, 'DarajaApp/phone.html')
  
class LnmApiGenericView(CreateAPIView):
    queryset = LNMOnline.objects.all()
   
   

    def create(self,request):
        print(request.data,"Successfull Morvin")


  


            # else:
            #     messages.info(request, f"Phone Number '{phone}' not a valid kenyan number/has a wrong format")
            


          

    