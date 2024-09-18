from django.forms import ModelForm
from shop.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "slime_quality"]
