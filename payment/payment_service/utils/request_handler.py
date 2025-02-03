import requests
from django.conf import settings
from ..helpers import token_handler

def make_authenticated_request(method, endpoint, **kwargs):
    access_token = token_handler.get_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = f'{settings.AUTH_SERVICE_BASE_URL}{endpoint}'
    response = requests.request(method, url, headers=headers, **kwargs)
    response.raise_for_status()
    return response.json()


def make_payment_request(product_id, product_name, product_quantity, product_price, user_name, user_email, user_cpf, user_id):
    url = "https://api.abacatepay.com/v1/billing/create"

    payload = {
        "frequency": "ONE_TIME",
        "methods": ["PIX"],
        "products": [
            {
                "externalId": product_id,
                "name": product_name,
                "quantity": product_quantity,
                "price": product_price
            }
        ],
        "customer":{
            "name": user_name,
            "email": user_email,
            "taxId": user_cpf,
        },
        "returnUrl": "http://0.0.0.0:8000/",
        "completionUrl": "http://0.0.0.0:8000/",   
        "customerId": user_id
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization" : "Bearer abc_dev_6631Q2zLsMf3pg1jeGf3U2Aj"
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()