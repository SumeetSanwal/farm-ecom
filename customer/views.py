from django.shortcuts import render
from farmer.models import *
from cart.forms import CartAddProductForm



# Create your views here.
def cust(request):
    name=request.session['username']
    return render(request,'customer.html',{'username':name})


def fruits(request):
    name = request.session['username']
    cart_f = CartAddProductForm()
    img = Product.objects.filter(cat='Fruits')    
    return render(request,'seeproducts.html',{'img':img,'cart_f':cart_f})


def vegetables(request):
    name = request.session['username']
    img = Product.objects.filter(cat='Vegetables')
    cart_f = CartAddProductForm()
    return render(request,'seeproducts.html',{'img':img,'cart_f':cart_f})


def grains(request):
    name = request.session['username']
    img = Product.objects.filter(cat='Grains')
    cart_f = CartAddProductForm()
    return render(request,'seeproducts.html',{'img':img,'cart_f':cart_f})



def poultry(request):
    name = request.session['username']
    img = Product.objects.filter(cat='Poulatry')

    cart_f = CartAddProductForm()
    return render(request,'seeproducts.html',{'img':img,'cart_f':cart_f})



def others(request):
    name = request.session['username']
    img = Product.objects.filter(cat='Other')
    cart_f = CartAddProductForm()
    return render(request,'seeproducts.html',{'img':img,'cart_f':cart_f})





