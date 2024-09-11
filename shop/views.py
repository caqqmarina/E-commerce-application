from django.shortcuts import render
from django.shortcuts import render, redirect

def show_shop(request):
    context = {
        'app_name': 'Online Slime Shop',
        'name': 'Chiara Aqmarina Diankusumo',
        'class': 'KKI'
    }
    return render(request, "main.html", context)


