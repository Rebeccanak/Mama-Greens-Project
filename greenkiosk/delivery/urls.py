from django.urls import path
from .views import delivery_upload_view
from .views import delivery_list
from .views import delivery_details
from .views import delivery_update_view
from .views import delete_delivery

urlpatterns = [
    path('delivery/upload/', delivery_upload_view, name='delivery_upload_view'),
    path('delivery/list/', delivery_list, name='delivery_list'),
    path('delivery/<int:id>/', delivery_details, name='delivery_details'),
    path('delivery/edit/<int:id>/', delivery_update_view, name='delivery_update_view'),
    path('delivery/delete/<int:id>/', delete_delivery, name='delete_delivery'),
]

