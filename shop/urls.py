from django.urls import path
from shop.views import show_shop
from shop.views import show_shop, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from shop.views import register
from shop.views import login_user
from shop.views import logout_user
from shop.views import edit_product_entry
from shop.views import delete_product_entry

app_name = 'shop'

urlpatterns = [
    path('', show_shop, name='show_shop'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product-entry/<uuid:id>', edit_product_entry, name='edit_product_entry'),
    path('delete-product/<uuid:id>/', delete_product_entry, name='delete_product_entry'),

]

