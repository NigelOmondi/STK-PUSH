from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from .models import MpesaResponse
import json

# Create your views here 07080635168

def index(request):
    cl = MpesaClient()
    phone_number = '0791869807'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

    # mpesa_response = MpesaResponse.objects.create(
    #     phone_number=phone_number,
    #     amount=amount,
    #     account_reference=account_reference,
    #     transaction_desc=transaction_desc,
    #     callback_url=callback_url,
    #     response=response,
    # )

    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        
        return HttpResponse("Simulating a C2B Transaction in Django👋")