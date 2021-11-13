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



from .models import TransactionDetails



def updatephone(request):
    if request.method == 'POST':
        phone = request.POST['phone']

                
        if len(phone) == 12 and phone.startswith("2547"):
            access_token = generate_access_token()
            api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
            headers = {"Authorization": "Bearer %s" %access_token }


            request = {    
                        "BusinessShortCode":bs_shortcode,    
                        "Password":decode_password(),    
                        "Timestamp":format_time(),    
                        "TransactionType": "CustomerPayBillOnline",    
                        "Amount":"1",    
                        "PartyA":phone,    
                        "PartyB":bs_shortcode,    
                        "PhoneNumber":phone,    
                        "CallBackURL": "https://rulibrary.heroku.com/update/lnm",
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

            return redirect('home-page')


        else:
            messages.info(request, f"Phone Number '{phone}' not a valid kenyan number/has a wrong format")
           


    return render(request, 'DarajaApp/phone.html')
    



 