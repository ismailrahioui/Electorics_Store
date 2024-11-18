from django.shortcuts import render,redirect
from django.db.models import Q , Count
from Store_app.models import *

def index (request):
    products= Product.objects.filter(status="Publish")

    context = {
        'product':products,
    }

    return render(request,"index.html",context)

def Products (request):
    products= Product.objects.filter(status="Publish")
    categories=  Categories.objects.annotate(product_count=Count('product'))
    colors=  Color.objects.all()
    filter_price= Filter_Price.objects.all()
    brand = Brand.objects.annotate(product_count=Count('product'))


    
    query= request.GET.get('query','')
    
    CATID=request.GET.get('Categories')
    FILID=request.GET.get('Filter_price')
    COLID=request.GET.get('Color')
    BRAID=request.GET.get('Brand')
    ATOZ=request.GET.get('AZ')
    ZTOA=request.GET.get('ZA')
    S_NEW=request.GET.get('new')
    S_OLD=request.GET.get('old')
    PIRCELOWTOHIGH=request.GET.get('PIRCELOWTOHIGH')
    PIRCEHIGHTOLOW=request.GET.get('PIRCEHIGHTOLOW')

    if CATID:
        products= Product.objects.filter(categories=CATID,status='Publish')
    elif FILID:
        products=Product.objects.filter(filter_price=FILID,status='Publish')
    elif COLID:
        products=Product.objects.filter(color=COLID,status='Publish')
    elif BRAID:
        products=Product.objects.filter(brand=BRAID,status='Publish')
    elif ATOZ:
        products=Product.objects.filter(status='Publish').order_by('name')
    elif ZTOA:
        products=Product.objects.filter(status='Publish').order_by('-name')
    elif S_NEW:
        products=Product.objects.filter(status='Publish').order_by('-created_date')
    elif S_OLD:
        products=Product.objects.filter(status='Publish').order_by('created_date')
    elif PIRCELOWTOHIGH:
        products=Product.objects.filter(status='Publish').order_by('price')
    elif PIRCEHIGHTOLOW:
        products=Product.objects.filter(status='Publish').order_by('-price')
    elif query:
        products=Product.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(information__icontains=query))
    else:
        products=Product.objects.filter(status='Publish')


    context = {
        'product':products,
        'category':categories ,
        'filter_price':filter_price,
        'color':colors,
        'brand':brand,
        
    }

    return render(request,"product/product.html",context)

def Product_details(request):
    return render (request,'product/product_detail.html')