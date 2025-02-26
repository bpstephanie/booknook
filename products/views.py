from django.shortcuts import render
from .models import Product, Book, Accessory

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    product_type = request.GET.get('type', 'all')

    if product_type == 'books':
        products = Book.objects.all()
        template = 'products/books.html'
    elif product_type == 'accessories':
        products = Accessory.objects.all()
        template = 'products/accessories.html'
    else:
        products = Product.objects.all()
        template = 'products/products.html'

    context = {
        'products': products,
    }

    return render(request, template, context)
