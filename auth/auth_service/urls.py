from django.urls import path  
from .views import LoginView, RegisterView, LogoutView, GetUsersView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', GetUsersView.as_view({'get': 'list'}), name='users'),
    path('users/<int:pk>/', GetUsersView.as_view({'get': 'retrieve'}), name='user')
]