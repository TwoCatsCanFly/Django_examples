from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home page')

def products(request):
    return HttpResponse('products page')

def customer(request):
    return HttpResponse('custumer page')
# Create your views here.
