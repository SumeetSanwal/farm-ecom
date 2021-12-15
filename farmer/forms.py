from django import forms
from .models import *
#
#
# class FruitForm(forms.ModelForm):
#     class Meta:
#         model = Fruit
#         fields = "__all__"
#
#
# class VegetablesForm(forms.ModelForm):
#     class Meta:
#         model = Vegetables
#         fields = "__all__"
#
# class GrainsForm(forms.ModelForm):
#     class Meta:
#         model = Grains
#         fields = "__all__"
#
#
# class PoulatryForm(forms.ModelForm):
#     class Meta:
#         model = Poulatry
#         fields = "__all__"
#
#
# class OtherForm(forms.ModelForm):
#     class Meta:
#         model = Other
#         fields = "__all__"
#
#
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

