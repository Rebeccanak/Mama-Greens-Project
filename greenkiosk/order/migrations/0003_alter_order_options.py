# Generated by Django 4.2.2 on 2023-06-30 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_order_status_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'order'},
        ),
    ]