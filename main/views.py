from django.shortcuts import render, redirect, get_object_or_404
from main.forms import Catalogue
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib import messages
import datetime
from django.urls import reverse
from django.utils.html import strip_tags
import json
import requests

# Create your views here.
def show_main(request): 
    context = {
        'app' : 'Ozon Sportswear',
        'name': request.user,
        'npm' : '2406420596',
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

# Login User
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

# Logout User
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def add_product(request):
    form = Catalogue(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_catalogue')

    context = {'form': form}
    return render(request, "add_product.html", context)

# Product Detail
@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
        
    context = {
        'product': product,
    }

    return render(request, "product_detail.html", context)

# Edit Product
@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = Catalogue(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_catalogue')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

# Show Catalogue
@login_required(login_url='/login')
def show_catalogue(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        # Return All Product Objects in Database
        product_list = Product.objects.all()
    elif filter_type == "featured":
        product_list = Product.objects.filter(is_featured=True)
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'product_list' : product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "catalogue.html", context)

# Delete Product
@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_catalogue'))

@login_required(login_url='/login')
def show_xml(request):
    product_list =Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, description_type="application/xml")

@login_required(login_url='/login')
def show_json(request):
    product_list = Product.objects.all()
    data=[
        {
            'id' : str(product.id),
            'name' : product.name,
            'price' : product.price,
            'description' : product.description,
            'thumbnail' : product.thumbnail,
            'category' : product.category,
            'is_featured' : product.is_featured, 
            'user_id' : product.user_id,
        }
        for product in product_list
    ]
    
    return JsonResponse(data, safe=False)

@login_required(login_url='/login')
def show_xml_by_id(request,product_id):
    try:
       product_item =Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml",product_item)
       return HttpResponse(xml_data, description_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)

@login_required(login_url='/login')
def show_json_by_id(request,product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data={
            'id' : str(product.id),
            'name' : product.name,
            'price' : product.price,
            'description' : product.description,
            'thumbnail' : product.thumbnail,
            'category' : product.category,
            'is_featured' : product.is_featured, 
            'user_id' : product.user_id,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
@csrf_exempt
@require_POST
@login_required(login_url='/login')
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name,
        price=price, 
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

# Delete Product via AJAX
@csrf_exempt
@require_POST
@login_required(login_url='/login')
def delete_product_entry_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return JsonResponse({'success': True}, status=200)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

# Edit Product via AJAX
@csrf_exempt
@require_POST
@login_required(login_url='/login')
def edit_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    product.name = request.POST.get("name", product.name)
    product.price = request.POST.get("price", product.price)
    product.description = request.POST.get("description", product.description)
    product.category = request.POST.get("category", product.category)
    product.thumbnail = request.POST.get("thumbnail", product.thumbnail)
    product.is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    product.user = request.user
    
    product.save()

    return HttpResponse(b"UPDATED", status=201)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def add_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))  # Strip HTML tags
        description = strip_tags(data.get("description", ""))  # Strip HTML tags
        price = data.get("price", 0)
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user
        
        new_product = Product(
            name = name,
            price = price,
            description = description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)