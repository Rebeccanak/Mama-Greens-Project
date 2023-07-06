from django.db import models

# Create your models here.
from django.db import models
class Delivery(models.Model):
    class Meta:
        verbose_name_plural = "delivery"
    customer_name = models.CharField(max_length=32)
    delivery_address = models.CharField(max_length=32)
    delivery_date = models.DateTimeField(auto_now_add=True)
    order_id = models.IntegerField()
    delivery_cost = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
