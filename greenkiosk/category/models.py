from django.db import models

# Create your models here.
from django.db import models
class Category(models.Model):
    class Meta:
        verbose_name_plural = "category"
    name = models.CharField(max_length=32, default='')
