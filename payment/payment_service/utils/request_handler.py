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