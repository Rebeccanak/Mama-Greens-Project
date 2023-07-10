from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer (models.Model):
    class Customer(models.Model):
        user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "customer"
    customer_id = models.PositiveIntegerField(default=0)
    first_name = models.CharField(max_length=32, default='')
    second_name = models.CharField(max_length=32,default='')
    email= models.EmailField(default='')
