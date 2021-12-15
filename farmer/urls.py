from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
        path('', views.farm, name='farm'),
        path('/home', views.farm, name='home'),
        path('/myproducts', views.myproducts, name='myproducts'),
        path('/add', views.add, name='add'),
        path('/account', views.account, name='account'),

]