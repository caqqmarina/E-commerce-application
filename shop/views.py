from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect   # Add import redirect at this line
from shop.forms import ProductEntryForm
from shop.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = Product.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            description=data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@login_required(login_url='/login')
def show_shop(request):
    context = {
        'app_name': 'Online Slime Shop',
        'name': request.user.username,
        'npm': '2306171480',
        'class': 'KKI',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False) 
        product_entry.user = request.user        
        product_entry.save()                    
        return redirect('shop:show_shop')        

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('shop:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("shop:show_shop"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
      else:
            messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)  # Logs out the current user
    response = HttpResponseRedirect(reverse('shop:login'))  # Redirect to the login page
    response.delete_cookie('last_login')  # Optional: delete the last login cookie
    return response

def edit_product_entry(request, id):
    # Get the product entry based on the provided ID
    product_entry = Product.objects.get(pk=id)

    # Set the product entry as an instance of the form (pre-filling the form)
    form = ProductEntryForm(request.POST or None, instance=product_entry)

    # Check if the form is valid and the request method is POST (form submission)
    if form.is_valid() and request.method == "POST":
        # Save the changes to the product entry
        form.save()
        # Redirect the user to the shop page (or wherever you want)
        return HttpResponseRedirect(reverse('shop:show_shop'))

    # Pass the form with the pre-filled product data to the template
    context = {'form': form}
    return render(request, "edit_product_entry.html", context)

def delete_product_entry(request, id):
    # Get the product entry based on the provided ID
    product_entry = Product.objects.get(pk=id)

    # Delete the product entry
    product_entry.delete()

    # Redirect the user to the shop page after deletion
    return HttpResponseRedirect(reverse('shop:show_shop'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    price = strip_tags(request.POST.get("price")) # strip HTML tags!
    description = request.POST.get("description")
    user = request.user
   
    new_product = Product(
        name=name, price=price,
        description=description,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
    
