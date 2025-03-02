from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Book, Accessory, Category, Genre
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower


# Create your views here.
def all_products(request, type=None):
    """ A view to show all products, including sorting and search queries """
    product_type = type if type else request.GET.get('type', 'all')
    query = request.GET.get('q') if 'q' in request.GET else None
    current_category = None
    # genres = None
    sort = None
    direction = None
    current_genre = None

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
            if sortkey == 'friendly_name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('friendly_name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category_names = request.GET.get('category').split(',')
            if product_type == 'accessories':
                products = products.filter(
                    category__friendly_name__in=category_names)
                current_category = Category.objects.filter(
                    friendly_name__in=category_names)
        if 'genre' in request.GET:
            genre_names = request.GET.get('genre').split(',')
            if product_type == 'books':
                products = products.filter(
                    genre__friendly_name__in=genre_names)
                current_genre = Genre.objects.filter(
                    friendly_name__in=genre_names)

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
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    current_sorting = f'{sort}_{direction}'

    categories = Category.objects.all()  # All categories
    genres = Genre.objects.all()  # All genres

    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'page_title': page_title,
        'type': product_type,
        'search_term': query,
        'current_category': current_category,
        'current_genre': current_genre,
        'all_categories': categories,
        'all_genres': genres,
        'is_paginated': page_obj.has_other_pages(),
        'current_sorting': current_sorting,
        'sort': sort,
        'direction': direction,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def all_genres(request):
    """ A view to show all genres on one page """
    all_genres = Genre.objects.prefetch_related('book_set').all()

    context = {
        'all_genres': all_genres,
        'page_title': 'All Book Genres'
    }

    return render(request, 'products/all_genres.html', context)


def all_categories(request):
    """ A view to show all accessory categories on one page """
    all_categories = Category.objects.prefetch_related('accessory_set').all()

    context = {
        'all_categories': all_categories,
        'page_title': 'All Accessory Categories'
    }

    return render(request, 'products/all_categories.html', context)
