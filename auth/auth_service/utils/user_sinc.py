import requests

def create_user_in_payment_service(user):
    data = {
        "user_id": user.id,
        "email": user.email,
        "username": user.username
    }
    try:
        response = requests.post("http://payment-service:8001/payment_service/user/sinc/", json=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        return response.status_code
    return response.status_code