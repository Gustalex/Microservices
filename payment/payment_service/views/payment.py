from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from payment_service.models import Payment
from payment_service.models import Product
from payment_service.serializers import PaymentSerializer
from ..helpers import get_user_info
from ..utils import make_payment_request
class PaymentViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=['post'], detail=False)
    def create_payment(self, request):
        user_id = request.user.id
        user_data = get_user_info(user_id)
        product = Product.objects.get(id=request.data['product_id'])
        product_name = product.product_name
        product_price = product.product_price
        product_quantity = request.data['product_quantity']
        user_name = user_data['name'] + ' ' + user_data['last_name']
        user_email = user_data['email']
        user_cpf = user_data['cpf']
        user_id = user_data['id']

        try:
            make_payment_request(product.id, product_name, product_quantity, product_price, user_name, user_email, user_cpf, user_id)
            payment = Payment.objects.create(
                related_user_name=user_name,
                product=product,
                payment_amount=product_price * product_quantity
            )
            serializer = PaymentSerializer(payment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
    @action(methods=['get'], detail=False)
    def list_payments(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
