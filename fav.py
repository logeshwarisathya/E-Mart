from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from myapp.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout
import json
from django.contrib.auth.decorators import login_required
import random

def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['pid']
      product_status=Product.objects.get(id=product_id)
      if product_status:
        if Favourite.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Favourite'}, status=200)
        else:
          Favourite.objects.create(user=request.user,product_id=product_id)
          return JsonResponse({'status':'Product Added to Favourite'}, status=200)
      
     
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
     return JsonResponse({'status':'Invalid Access'}, status=200)