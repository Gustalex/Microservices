from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
import requests
from decouple import config

AUTH_SERVICE_URL = config('AUTH_SERVICE_URL')
SERVICE_EMAIL = config('SERVICE_EMAIL')
SERVICE_PASSWORD = config('SERVICE_PASSWORD')

def get_service_token():
    token = cache.get("service_token")

    if not token:
        data = {
            "email": SERVICE_EMAIL,
            "password": SERVICE_PASSWORD
        }
        response = requests.post(AUTH_SERVICE_URL, json=data)
        response.raise_for_status()
        token = response.json().get("access")

        cache.set("service_token", token, timeout=7200) 

    return token

class ServiceAuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if not request.headers.get("Authorization"):
            request.META["HTTP_AUTHORIZATION"] = f"Bearer {get_service_token()}"
