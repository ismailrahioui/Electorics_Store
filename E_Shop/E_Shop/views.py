from django.shortcuts import render,redirect
from Store_app.models import *

def index (request):
    products= Product.objects.filter(status="Publish")

    context = {
        'product':products,
    }

    return render(request,"index.html",context)

def Products (request):
    products= Product.objects.filter(status="Publish")
    categories=  Categories.objects.all()
    colors=  Color.objects.all()
    filter_price= Filter_Price.objects.all()

    context = {
        'product':products,
        'category':categories ,
        'filter_price':filter_price,
        'color':colors,
    }

    return render(request,"product/product.html",context)
