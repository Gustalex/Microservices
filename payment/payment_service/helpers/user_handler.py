from ..utils import make_authenticated_request

def get_user_info(user_id):
    endpoint = f'/auth/users/{user_id}/'
    return make_authenticated_request('get', endpoint)
