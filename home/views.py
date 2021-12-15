from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .forms import *
from cart.cart import Cart


def home(request):
    if request.method == "POST":
        p=request.POST['select']
        if(p=='farmer'):
            f = {'fname': request.POST['name'], 'fmail': request.POST['email'], 'fphone': request.POST['phone'],
                 'fpassword': request.POST['pass'], 'profession': request.POST['select']}
            form=FarmerForm(f)
        else:
            f = {'cname': request.POST['name'], 'cmail': request.POST['email'], 'cphone': request.POST['phone'],
                 'cpassword': request.POST['pass'], 'profession': request.POST['select']}
            form=CustomerForm(f)
        if not User.objects.filter(username=request.POST['name']):
                user=User.objects.create_user(username=request.POST['name'],password=request.POST['pass'])
                user.save()
                form.save()

    return render(request,"index.html")


def login(request):

    if request.method == "POST":
        name = request.POST['your_name']
        password = request.POST['your_pass']
        profession = request.POST['select']
        user=auth.authenticate(username=name,password=password)
        request.session['username']=name
        if user is not None:
            cart = Cart(request)
            cart.clear()
            # request.session['username']=name
            if profession=='customer':
                # return redirect("/customer")
                return render(request,"customer.html",{'username':name})
            else:
                # return redirect("/farmer")
                return render(request, "farmer.html", {'username': name})
        else:
            return redirect("login")
    else:
        return render(request, "index.html")
