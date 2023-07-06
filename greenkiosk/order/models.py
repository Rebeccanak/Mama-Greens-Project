from django.db import models

# Create your models here.from django.db import models
class Order(models.Model):
    class Meta:
        verbose_name_plural = "order"
    order_status = models.CharField(max_length=32)
    items = models.CharField(max_length=10)
    customer_information  = models.CharField(max_length=15)
    payment_details = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    

