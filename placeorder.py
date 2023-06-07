from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from myapp.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout
import json
from django.contrib.auth.decorators import login_required
import random

@login_required(login_url="/login/")
def placeorder(request):
  if request.method == 'POST':
    neworder=Order()
    neworder.user=request.user
    neworder.fname=request.POST.get('fname')
    neworder.lname=request.POST.get('lname')
    neworder.email=request.POST.get('email')
    neworder.phone=request.POST.get('phone')
    neworder.address=request.POST.get('address')
    neworder.city=request.POST.get('city')
    neworder.state=request.POST.get('state')
    neworder.country=request.POST.get('country')
    neworder.pincode=request.POST.get('pincode')

    neworder.payment_mode=request.POST.get('payment_mode')

    cart=Cart.objects.filter(user=request.user)
    cart_total_price = 0
    for item in cart:
      cart_total_price = cart_total_price + item.product.selling_price * item.product_qty

    neworder.total_price = cart_total_price
    trackno = 'sharma'+str(random.randint(1111111,9999999))
    while Order.objects.filter(tracking_no=trackno) is None:
      trackno = 'sharma'+str(random.randint(1111111,9999999))

    neworder.tracking_no= trackno
    neworder.save()

    neworderitems = Cart.objects.filter(user=request.user)
    for item in neworderitems:
      OrderItem.objects.create(
        order=neworder,
        product=item.product,
        price=item.product.selling_price,
        quantity=item.product_qty
      )

      # To decrease the product quantity from available stock
      orderproduct = Product.objects.filter(id=item.product_id).first()
      orderproduct.quantity=orderproduct.quantity - item.product_qty
      orderproduct.save()

    # To clear user's Cart
    Cart.objects.filter(user=request.user).delete()

    messages.success(request,"Your order has been placed successfully")


  return redirect('/')