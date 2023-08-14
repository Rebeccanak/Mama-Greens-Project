from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import CartUploadForm
from Cart.models import Cart


def cart_upload_view(request):
    if request.method == 'POST':
        form = CartUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else: 
        form = CartUploadForm()
    return render(request, 'cart/upload_cart.html', {'form': form})

def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'cart/cart_list.html', {'carts': carts})

def cart_details(request, id):
    cart = Cart.objects.get(id=id)
    return render(request, 'cart/cart_details.html', {'cart': cart})

def cart_update_view(request, id):
    cart = Cart.objects.get(id=id)

    if request.method == 'POST':
        form = CartUploadForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect('cart_details', id=cart.id)
    
    else:
        form = CartUploadForm(instance=cart)

    return render(request, 'cart/edit_cart.html', {'form': form})

def delete_cart(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('cart_list')
