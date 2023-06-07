from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from myapp.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout
import json
from django.contrib.auth.decorators import login_required
import random

def product_details(request,cname,pname):
  if(Catagory.objects.filter(name=cname,status=0)):
     if(Product.objects.filter(name=pname,status=0)):
        products=Product.objects.filter(name=pname,status=0).first()
        return render(request,"shop/products/product_details.html",{"products":products})
     else:
        messages.warning(request,"No Such Product Found")
        return redirect('collections')


  else:
    messages.warning(request,"No Such Catagory Found")
    return redirect('collections')