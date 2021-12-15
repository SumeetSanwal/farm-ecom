from django.db import models

# Create your models here.
class Farmer(models.Model):
    fname=models.CharField(max_length=30)
    fmail=models.EmailField()
    fphone=models.CharField(max_length=10)
    fpassword=models.CharField(max_length=30)
    profession=models.CharField(max_length=30)
    class Meta:
        db_table="farmer"


class Customer(models.Model):
    cname=models.CharField(max_length=30)
    cmail=models.EmailField()
    cphone=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=30)
    profession = models.CharField(max_length=30)
    class Meta:
        db_table="customer"
