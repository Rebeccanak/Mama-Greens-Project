from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import DeliveryUploadForm
from .models import Delivery

def delivery_upload_view(request):
    if request.method == 'POST':
        form = DeliveryUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('delivery_list')
    else: 
        form = DeliveryUploadForm()
    return render(request, 'delivery/upload_delivery.html', {'form': form})

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'delivery/delivery_list.html', {'deliveries': deliveries})

def delivery_details(request, id):
    delivery = Delivery.objects.get(id=id)
    return render(request, 'delivery/delivery_details.html', {'delivery': delivery})

def delivery_update_view(request, id):
    delivery = Delivery.objects.get(id=id)

    if request.method == 'POST':
        form = DeliveryUploadForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect('delivery_details', id=delivery.id)
    
    else:
        form = DeliveryUploadForm(instance=delivery)

    return render(request, 'delivery/edit_delivery.html', {'form': form})

def delete_delivery(request, id):
    delivery = Delivery.objects.get(id=id)
    delivery.delete()
    return redirect('delivery_list')
