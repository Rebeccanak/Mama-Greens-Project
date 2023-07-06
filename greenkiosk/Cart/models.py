from django.db import models

# Create your models here.
class Cart(models.Model):
    class Meta:
        verbose_name_plural = "Cart"
    product_name = models.CharField(max_length=32)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_image =models.ImageField()
    date_added = models.DateTimeField()


