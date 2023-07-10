from django.db import models
from Cart.models import Cart
from customer.models import Customer
from delivery.models import Delivery


# Create your models here.from django.db import models
class Order(models.Model):

    class Meta:
        verbose_name_plural = "order"
    basket = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.CASCADE )
    #  delivery = models.

    order_status = models.CharField(max_length=32)
    items = models.CharField(max_length=10)
    customer_information  = models.CharField(max_length=15)
    payment_details = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    

