from django.forms import ModelForm
from shop.models import Product
from django import forms

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "slime_quality"]
        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)

        def clean_price(self):
            price = self.cleaned_data["price"]
            return strip_tags(price)

# class ProductEntryForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'price', 'description', 'slime_quality']
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
#             }),
#             'price': forms.NumberInput(attrs={
#                 'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
#             }),
#             'description': forms.Textarea(attrs={
#                 'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
#             }),
#             'slime_quality': forms.Select(attrs={
#                 'class': 'w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
#             }),
#         }