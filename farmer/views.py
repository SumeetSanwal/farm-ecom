from django.shortcuts import render,redirect
from .forms import *
from .models import *


# Create your views here.
def farm(request):
    name = request.session['username']
    return render(request,'farmer.html',{'username':name})


def myproducts(request):
    name = request.session['username']
    img = Product.objects.filter(seller=name,cat='Fruits')
    img2 = Product.objects.filter(seller=name, cat='Vegetables')
    img3 = Product.objects.filter(seller=name, cat='Grains')
    img4 = Product.objects.filter(seller=name,cat='Poulatry')
    img5 = Product.objects.filter(seller=name,cat='Other')
    return render(request, "myproducts.html", {"img": img,"img2": img2,"img3": img3,"img4": img4,"img5": img5})



def account(request):
    name = request.session['username']
    return render(request,'farmer.html',{'username':name})


def add(request):

    name = request.session['username']

    if request.method == "POST":

        f = {'seller': name, 'prodname': request.POST['prodname'], 'price': int(request.POST['price']),
                 'cat':request.POST['cat'],'image': request.FILES['image']}
        form2 = ProductForm(data=f, files=request.FILES)
        if form2.is_valid():
           form2.save()

        # if cat=='Fruits':
        #     f={'seller':name,'prodname':request.POST['prodname'],'price':int(request.POST['price']), 'image': request.FILES['image']}
        #     form = FruitForm(data=f,files=request.FILES)
        #     form2=ProductForm(data=f,files=request.FILES)
        #     if form.is_valid():
        #         form2.save()
        #         form.save()
        #
        #
        #
        # elif cat=='Vegetables':
        #     f = {'seller': name, 'prodname': request.POST['prodname'], 'price': int(request.POST['price']),
        #          'image': request.FILES['image']}
        #     form = VegetablesForm(data=f, files=request.FILES)
        #     form2 = ProductForm(data=f, files=request.FILES)
        #     if form.is_valid():
        #         form2.save()
        #         form.save()
        #
        #
        # elif cat=='Grains':
        #     f = {'seller': name, 'prodname': request.POST['prodname'], 'price': int(request.POST['price']),
        #          'image': request.FILES['image']}
        #     form = GrainsForm(data=f, files=request.FILES)
        #     form2 = ProductForm(data=f, files=request.FILES)
        #     if form.is_valid():
        #         form2.save()
        #         form.save()
        #
        #
        # elif cat=='Poulatry':
        #     f = {'seller': name, 'prodname': request.POST['prodname'], 'price': int(request.POST['price']),
        #          'image': request.FILES['image']}
        #     form = PoulatryForm(data=f, files=request.FILES)
        #     form2 = ProductForm(data=f, files=request.FILES)
        #     if form.is_valid():
        #         form2.save()
        #         form.save()
        #
        # else:
        #     f = {'seller': name, 'prodname': request.POST['prodname'], 'price': int(request.POST['price']),
        #          'image': request.FILES['image']}
        #     form = OtherForm(data=f, files=request.FILES)
        #     form2 = ProductForm(data=f, files=request.FILES)
        #     if form.is_valid():
        #         form2.save()
        #         form.save()
        #
        #
        #

    return render(request,'addproduct.html')