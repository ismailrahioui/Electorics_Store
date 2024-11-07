from django.shortcuts import render,redirect
from Store_app.models import *

def index (request):
    products= Product.objects.filter(status="Publish")

    context = {
        'product':products,
    }

    return render(request,"index.html",context)
