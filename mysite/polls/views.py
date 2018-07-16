from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world. You're at the polls index.</h1>")