from django.db import models 

class Payment(models.Model):
    related_user_name = models.CharField(max_length=50)
    payment_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.related_user_name
    
    class Meta:
        db_table = 'payment'
        ordering = ['-created_at']