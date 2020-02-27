from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def reg_page(request):
    return render(request, 'register.html')

def homepage(request):
    return render(request, 'homepage.html')

def logout(request):
    # request.session.clear()
    return redirect('/')