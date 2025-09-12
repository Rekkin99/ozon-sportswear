from django.shortcuts import render, redirect, get_object_or_404
from main.forms import Catalogue
from main.models import Product

# Create your views here.
def show_main(request):
    # Return All Product Objects in Database
    product_list = Product.objects.all()

    context = {
        'app' : 'Ozon Sportswear',
        'name': 'Farrell Bagoes Rahmantyo',
        'npm' : '2406420596',
        'product_list' : product_list 
    }

    return render(request, "main.html", context)

def add_product(request):
    form = Catalogue(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    

    context = {
        'product': product,
        'price' : "Rp. {:,}".format(product.price)
    }

    return render(request, "product_detail.html", context)