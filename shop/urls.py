from django.urls import path
from shop.views import show_shop

app_name = 'shop'

urlpatterns = [
    path('', show_shop, name='show_shop'),
]

