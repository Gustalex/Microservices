import requests
from decouple import config

AUTH_SERVICE_URL = config('AUTH_SERVICE_URL')
SERVICE_EMAIL = config('SERVICE_EMAIL')
SERVICE_PASSWORD = config('SERVICE_PASSWORD')

def get_token():
    data = {
        "email": SERVICE_EMAIL,
        "password": SERVICE_PASSWORD
    }
    response = requests.post(AUTH_SERVICE_URL, json=data)
    response.raise_for_status()
    return response.json()['access']