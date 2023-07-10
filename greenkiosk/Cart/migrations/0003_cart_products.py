# Generated by Django 3.2.12 on 2023-07-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_product_options'),
        ('Cart', '0002_alter_cart_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='inventory.Product'),
        ),
    ]
