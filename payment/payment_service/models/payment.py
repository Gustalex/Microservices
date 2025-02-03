from django.db import models 
from .product import Product

class Payment(models.Model):
    related_user_name = models.CharField(max_length=50)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.related_user_name
    
    class Meta:
        db_table = 'payment'
        ordering = ['-created_at']