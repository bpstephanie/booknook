from django.shortcuts import render, get_object_or_404
from .models import Product, Book, Accessory
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def all_products(request, type=None):
    """ A view to show all products, including sorting and search queries """
    product_type = type if type else request.GET.get('type', 'all')
    query = request.GET.get('q', '')

    # Initialize an empty queryset
    products = Product.objects.none()

    if product_type == 'books':
        products = Book.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        page_title = 'All Books'
    elif product_type == 'accessories':
        products = Accessory.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        page_title = 'All Accessories'
    else:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        page_title = 'All Products'

    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'page_title': page_title,
        'query': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
