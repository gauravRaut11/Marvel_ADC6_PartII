
from django.shortcuts import render
from .models import Order, Cart
from index.models import Item
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse

def get_user_pending_order(request):
    user_profile = get_object_or_404(User, username=request.user)
    order = Cart.objects.filter(user=user_profile)
    if order.exists():
        return order[0]

    return 0


def add_to_cart(request,pk):
    user_profile = get_object_or_404(User, username=request.user)
    products = Item.objects.get(pk=pk)
    order_item, status = Order.objects.get_or_create(products=products)
    user_order, status = Cart.objects.get_or_create(user=user_profile)
    user_order.items.add(order_item)
    
    if status:
        user_order.save()
    
    return redirect(reverse('carts'))


def delete_from_cart(request,id):
    item_to_delete = Order.objects.filter(pk=id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
    return redirect(reverse('carts'))


def cart_details(request):
    show_order = get_user_pending_order(request)
    context = {
        'order':show_order
    }
    return render(request,'cart.html',context)