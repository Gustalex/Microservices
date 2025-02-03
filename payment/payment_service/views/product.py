from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from payment_service.models import Product
from payment_service.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    