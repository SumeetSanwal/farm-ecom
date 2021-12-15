from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'orders'

urlpatterns = [
	path(r'', views.od, name='od'),
	path(r'/myorder', views.myorder, name='myorder'),
	path(r'/checkout', views.order_create, name='order_create'),

]

