from django.db import models

# Create your models here.
# class Fruit(models.Model):
#     seller = models.CharField(max_length=30)
#     prodname=models.CharField(max_length=30)
#     price=models.IntegerField()
#     image=models.ImageField(upload_to='pics')
#     class Meta:
#         db_table="fruit"
#
# class Vegetables(models.Model):
#     seller = models.CharField(max_length=30)
#     prodname=models.CharField(max_length=30)
#     price=models.IntegerField()
#     image=models.ImageField(upload_to='pics')
#     class Meta:
#         db_table="vegetables"
#
# class Grains(models.Model):
#     seller = models.CharField(max_length=30)
#     prodname=models.CharField(max_length=30)
#     price=models.IntegerField()
#     image=models.ImageField(upload_to='pics')
#     class Meta:
#         db_table="grains"
#
# class Poulatry(models.Model):
#     seller = models.CharField(max_length=30)
#     prodname=models.CharField(max_length=30)
#     price=models.IntegerField()
#     image=models.ImageField(upload_to='pics')
#     class Meta:
#         db_table="poulatry"
#
# class Other(models.Model):
#     seller = models.CharField(max_length=30)
#     prodname=models.CharField(max_length=30)
#     price=models.IntegerField()
#     image=models.ImageField(upload_to='pics')
#     class Meta:
#         db_table="other"

class Product(models.Model):
    cat=models.CharField(max_length=30)
    seller = models.CharField(max_length=30)
    prodname=models.CharField(max_length=30)
    price=models.IntegerField()
    image=models.ImageField(upload_to='pics')
    class Meta:
        db_table="product"