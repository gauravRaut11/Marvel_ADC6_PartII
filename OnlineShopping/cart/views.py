
from django.shortcuts import render
from .models import Order, OrderItem
from index.models import Item
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse


def add_to_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user
    )
    order = Order.objects.create(
        user=request.user)
    order.items.add(order_item)
    return redirect("carts")

def delete_from_cart(request,id):
    item_to_delete = Order.objects.filter(pk=id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
    return redirect(reverse('carts'))


def cart_details(request):
    show_order = Order.objects.get(user=request.user, ordered=False)
    context = {
        'order':show_order
    }
    return render(request,'cart.html',context)