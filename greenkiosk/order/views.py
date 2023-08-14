# from django.shortcuts import render

# # Create your views here.

# from django.shortcuts import render , redirect
# from .forms import OrderUploadForm
# from .models import Order


# # Create your views here.

# def order_upload_view(request):
#     if request.method == 'POST':
#         form = OrderUploadForm(request.POST)
#         # form = ProductUploadForm(request.data, request.Files)
#         if form.is_valid():
#             form.save()
#     else: 
#         form = OrderUploadForm()
#     return render(request,"order/upload_order.html",{"form":form})



# def order_list(request):
#     orders = Order.objects.all()
#     return render(request, 'order/order_list.html', {'orders':orders})


# def order_details(request , id):
#     order = Order.objects.get(id=id)
#     return render(request , 'order/order_details.html',{'order':order})




# def order_update_view(request, id):
#     order = Order.objects.get(id=id)

#     if request.method == 'POST':
#         form = OrderUploadForm(request.POST, instance=order)

#         if form.is_valid():
#             form.save()
#             return redirect("order_details", id=order.id)
    
#     else:
#         form = OrderUploadForm(instance=order)

#     return render(request, "order/edit_order.html", {'form': form})

# def delete_order(request, id):
#     order= Order.objects.get(id=id)
#     order.delete()
#     return redirect("order_list_view")



from django.shortcuts import render, redirect
from .forms import OrderUploadForm
from .models import Order

def order_upload_view(request):
    if request.method == 'POST':
        form = OrderUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else: 
        form = OrderUploadForm()
    return render(request, 'order/upload_order.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})

def order_details(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'order/order_details.html', {'order': order})

def order_update_view(request, id):
    order = Order.objects.get(id=id)

    if request.method == 'POST':
        form = OrderUploadForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_details', id=order.id)
    
    else:
        form = OrderUploadForm(instance=order)

    return render(request, 'order/edit_order.html', {'form': form})

def delete_order(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('order_list')
