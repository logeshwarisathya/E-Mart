from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from myapp.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout
import json
from django.contrib.auth.decorators import login_required
import random

def checkout(request):
  rawcart=Cart.objects.filter(user=request.user)
  for item in rawcart:
    if item.product_qty > item.product.quantity :
      Cart.objects.filter(user=request.user).delete()

      # Cart.objects.delete(id=item.id)

  cartitems = Cart.objects.filter(user=request.user)
  total_price = 0
  for item in cartitems:
    total_price = total_price + item.product.selling_price * item.product_qty    

  context={'cartitems':cartitems,'total_price':total_price}
  return render(request,"shop/checkout.html",context)