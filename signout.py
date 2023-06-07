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
def signout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/login")