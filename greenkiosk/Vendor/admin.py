from django.contrib import admin

# Register your models here.

from .models import Vendor
# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
admin.site.register(Vendor, VendorAdmin)