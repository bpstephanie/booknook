from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Book, Accessory, Category, Genre
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def all_products(request, type=None):
    """ A view to show all products, including sorting and search queries """
    product_type = type if type else request.GET.get('type', 'all')
    query = request.GET.get('q') if 'q' in request.GET else None
    categories = None
    genres = None
    sort = None
    direction = None

    # Initialize the products queryset based on type
    if product_type == 'books':
        products = Book.objects.all()
        page_title = 'All Books'
    elif product_type == 'accessories':
        products = Accessory.objects.all()
        page_title = 'All Accessories'
    else:
        products = Product.objects.all()
        page_title = 'All Products'

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:  # and product_type == 'accessories':
            category_names = request.GET.get('category').split(',')
            if product_type == 'accessories':
                products = products.filter(category__name__in=category_names)
                categories = Category.objects.filter(name__in=category_names)
        if 'genre' in request.GET:  # and product_type == 'books':
            genre_names = request.GET.get('genre').split(',')
            products = products.filter(genre__name__in=genre_names)
            genres = Genre.objects.filter(name__in=genre_names)

        if 'q' in request.GET:
            query = request.GET.get('q')
            if not query:
                messages.error(request, "You didn't search for anything")
                return redirect(reverse('products'))

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        if not products.exists():
            messages.error(request, 'No products match your search criteria')
            return redirect(reverse('products'))

    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'page_title': page_title,
        'search_term': query,
        'current_categories': categories,
        'current_genres': genres,
        'is_paginated': page_obj.has_other_pages(),
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
