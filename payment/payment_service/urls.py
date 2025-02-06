from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, ProductViewSet, CreateUserView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('payments/create/', PaymentViewSet.as_view({'post': 'create_payment'}), name='create_payment'),
    path('payments/list/', PaymentViewSet.as_view({'get': 'list_payments'}), name='list_payments'),
    path('user/sinc/', CreateUserView.as_view(), name='user_sinc'),
]