from django.urls import path
from main.views import show_main, add_product, show_product, show_catalogue,show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, edit_product, delete_product, add_product_entry_ajax
from main.views import edit_product_entry_ajax, delete_product_entry_ajax, proxy_image, add_product_flutter, show_my_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product/', add_product, name='add_product'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('catalogue/', show_catalogue, name='show_catalogue'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('edit-product-ajax/<uuid:id>/', edit_product_entry_ajax, name='edit_product_entry_ajax'),
    path('delete-product-ajax/<uuid:id>/', delete_product_entry_ajax, name='delete_product_entry_ajax'),
    path('proxy-image/', proxy_image, name='proxt-image'),
    path('add-product-flutter/', add_product_flutter, name='add-product-flutter'),
    path('json/my/', show_my_json, name='show_my_json')
]