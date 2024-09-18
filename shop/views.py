from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect   # Add import redirect at this line
from shop.forms import ProductEntryForm
from shop.models import Product
from django.http import HttpResponse
from django.core import serializers


def show_shop(request):
    product_entries = Product.objects.all()

    context = {
        'app_name': 'Online Slime Shop',
        'name': 'Chiara Aqmarina Diankusumo',
        'npm': '2306171480',
        'class': 'KKI',
        'product_entries': product_entries,
    }
    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('shop:show_shop')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


