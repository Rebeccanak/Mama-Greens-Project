from django.contrib import admin

# Register your models here.
from.models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=("customer_id","first_name","second_name","email")
admin.site.register(Customer,CustomerAdmin)

