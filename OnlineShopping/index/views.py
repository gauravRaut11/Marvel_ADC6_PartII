from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item
from shopping_cart.models import Order
from django.db.models import Q

def home(request):
    items=Item.objects.all()
    filtered_orders=Order.objects.filter(owner=request.user.profile,is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_products = [product.Item for product in user_order_items]

    context = {
        'items':items,
        'current_order_products': current_order_products
    }
    return render(request,'home.html',context)

def upload_item(request):
    return render(request,'upload.html')
    

def upload(request):
    image=request.FILES['image']
    product_name=request.POST['product_name']
    category=request.POST['category']
    price=request.POST['price']
    items=Item(image=image, product_name=product_name, category=category, price=price)
    items.save()
    return redirect('/')

def search(request):
    if request.method == "GET":
        src=request.GET['search']
        match=Item.objects.filter(Q(product_name__startswith=src)) 
        if match:
            return render(request,'home.html',{'source':match})
        else:
            return HttpResponse('notResponse')
    
def delete(request, pk):
    items=Item.objects.get(pk=pk)
    items.delete()
    return redirect("/")

def update_form(request, pk):
    items=Item.objects.get(pk=pk)
    return render(request,'edit.html',{'items':items})

def update(request, pk):
    items=Item.objects.get(pk=pk)
    if request.method=="POST":
        items.image=request.FILES['image']
        items.product_name=request.POST['product_name']
        items.category=request.POST['category']
        items.price=request.POST['price']
        items.save()
        return redirect("/")

    else:
        return HttpResponse("record not updated")





