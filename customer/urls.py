from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
        path('', views.cust, name='cust'),
        path('/home', views.cust, name='cust'),
        path('/fruits', views.fruits, name='fruits'),
        path('/vegetables', views.vegetables, name='vegetables'),
        path('/grains', views.grains, name='grains'),
        path('/others', views.others, name='others'),
        path('/poultry', views.poultry, name='poultry'),

]