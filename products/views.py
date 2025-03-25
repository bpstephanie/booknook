from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from .models import (
    Product, Book, Accessory, Category, Genre, Review
)
from wishlist.models import Wishlist, WishlistItem
from .forms import ReviewForm, BookForm, AccessoryForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower


# Create your views here.
def all_products(request, type=None):
    """ A view to show all products, including sorting and search queries """
    product_type = type if type else request.GET.get('type', 'all')
    query = request.GET.get('q') if 'q' in request.GET else None
    current_category = None
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
                products = products.annotate(
                    lower_name=Lower('friendly_name')
                ).order_by(sortkey, 'name')

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

    categories = Category.objects.all()
    genres = Genre.objects.all()

    user_wishlists = []
    wishlist_items = []
    if request.user.is_authenticated:
        user_wishlists = Wishlist.objects.filter(user=request.user)
        wishlist_items = WishlistItem.objects.filter(
            wishlist__user=request.user).values_list('product_id', flat=True)

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
        'user_wishlists': user_wishlists,
        'wishlist_items': wishlist_items,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = None

    approved_reviews = product.reviews.filter(approved=True)

    if request.user.is_authenticated:
        user_reviews = product.reviews.filter(author=request.user)
        approved_reviews = product.reviews.filter(approved=True)
        reviews = user_reviews | approved_reviews
    else:
        reviews = product.reviews.filter(approved=True)

    review_count = approved_reviews.count()

    review_form = ReviewForm()

    user_wishlists = []
    has_purchased = False

    if request.user.is_authenticated:
        user_wishlists = Wishlist.objects.filter(user=request.user)
        wishlist_item = WishlistItem.objects.filter(
            wishlist__user=request.user, product=product).first()
        has_purchased = request.user.userprofile.has_purchased(product)
    else:
        has_purchased = False

    if request.method == "POST":
        if 'review_submit' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.author = request.user
                review.product = product
                review.save()
                messages.success(request, 'Review submitted successfully!')
                return redirect('product_detail', product_id=product.id)
            else:
                messages.error(
                    request,
                    (
                        'There was an error submitting your review. '
                        'Please check the form and try again.'
                    ))

    paginator = Paginator(reviews, 10)
    page_number = request.GET.get('page', 1)
    reviews = paginator.get_page(page_number)

    context = {
        'product': product,
        'reviews': reviews,
        'review_count': review_count,
        'review_form': review_form,
        'user_wishlists': user_wishlists,
        'wishlist_item': wishlist_item,
        'has_purchased': has_purchased,
    }

    return render(request, 'products/product_detail.html', context)


def all_genres(request):
    """ A view to show all genres on one page """
    sort = None
    direction = None

    all_genres = Genre.objects.prefetch_related('book_set').order_by('name')

    for genre in all_genres:
        genre.sorted_books = genre.book_set.all()
        genre.book_count = genre.sorted_books.count()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'friendly_name':
                sortkey = 'lower_name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            for genre in all_genres:
                books = genre.book_set.all()
                if sortkey == 'lower_name':
                    books = books.annotate(lower_name=Lower('friendly_name'))
                genre.sorted_books = books.order_by(sortkey)

    context = {
        'all_genres': all_genres,
        'page_title': 'All Book Genres',
        'sort': sort,
        'direction': direction,
        'current_sorting': (
            f'{sort}_{direction}' if sort and direction else None
        ),
    }

    return render(request, 'products/all_genres.html', context)


def all_categories(request):
    """ A view to show all accessory categories on one page """
    sort = None
    direction = None

    all_categories = Category.objects.prefetch_related(
        'accessory_set').order_by('name')

    for category in all_categories:
        category.sorted_accessories = category.accessory_set.all()
        category.accessory_count = category.sorted_accessories.count()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'friendly_name':
                sortkey = 'lower_name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            for category in all_categories:
                accessories = category.accessory_set.all()
                if sortkey == 'lower_name':
                    accessories = accessories.annotate(
                        lower_name=Lower('friendly_name')
                    )
                category.sorted_accessories = accessories.order_by(sortkey)

    context = {
        'all_categories': all_categories,
        'page_title': 'All Accessory Categories',
        'sort': sort,
        'direction': direction,
        'current_sorting': (
            f'{sort}_{direction}' if sort and direction else None
        ),
    }

    return render(request, 'products/all_categories.html', context)


@login_required
def submit_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if not request.user.userprofile.has_purchased(product):
        return HttpResponseForbidden(
            'You can only review products you have purchased.'
        )

    if request.method == "POST":
        review_id = request.POST.get('review_id')
        if review_id:
            review = get_object_or_404(
                Review, id=review_id, author=request.user)
            form = ReviewForm(request.POST, instance=review)
        else:
            form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            messages.success(request, "Review submitted successfully")
            return redirect('product_detail', product_id=product.id)
        else:
            messages.error(
                request,
                ("There was an error submitting your review. Please check the "
                 "form and try again."))
    else:
        form = ReviewForm()
    return render(request, 'submit_review.html', {'form': form})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, author=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.approved = False
            review.save()
            messages.success(request, 'Review Updated!')
            next_url = request.POST.get('next', 'product_detail')
            if next_url == 'profile':
                return redirect('profile', section='userReviews')
            else:
                return redirect('product_detail', product_id=review.product.id)
        else:
            messages.error(
                request, 'Error updating review!'
            )
    else:
        form = ReviewForm(instance=review)

    next_url = request.GET.get('next', 'product_detail')
    if next_url == 'profile':
        template = 'profiles/edit_review.html'
    else:
        template = 'products/edit_review.html'

    return render(request, template, {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(
        Review, id=review_id, author=request.user
    )
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect('product_detail', product_id=review.product.id)


@login_required
def product_management(request):
    """ Displays product management page """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only authorised personnel can do that.')
        return redirect(reverse('home'))

    book_form = BookForm()
    accessory_form = AccessoryForm()
    section = request.GET.get('section', '')

    template = 'products/product_management.html'
    context = {
        'book_form': book_form,
        'accessory_form': accessory_form,
        'section': section,
    }
    return render(request, template, context)


@login_required
def add_book(request):
    """ Add a book to the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only authorised personnel can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(
                request, f'Successfully added {book.friendly_name}!')
            return redirect(reverse('product_detail', args=[book.id]))
        else:
            messages.error(
                request, (
                    'Failed to add book. Please ensure the form is valid.'
                ))
    else:
        form = BookForm()
    return redirect('product_management')


@login_required
def add_accessory(request):
    """ Add an accessory to the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only authorised personnel can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AccessoryForm(request.POST, request.FILES)
        if form.is_valid():
            accessory = form.save()
            messages.success(
                request, f'Successfully added {accessory.friendly_name}!')
            return redirect(reverse('product_detail', args=[accessory.id]))
        else:
            messages.error(
                request, (
                    'Failed to add accessory. Please ensure the form is valid.'
                ))
    else:
        form = AccessoryForm()
    return redirect('product_management')


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only authorised personnel can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if hasattr(product, 'book'):
        product = get_object_or_404(Book, pk=product_id)
        form_class = BookForm
        template = 'products/edit_book.html'
        product_type = 'Book'
    elif hasattr(product, 'accessory'):
        product = get_object_or_404(Accessory, pk=product_id)
        form_class = AccessoryForm
        template = 'products/edit_accessory.html'
        product_type = 'Accessory'
    else:
        messages.error(request, 'Invalid product type.')
        return redirect('product_management')

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Successfully updated {product.friendly_name}!')
            return redirect('product_detail', product_id=product.id)
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = form_class(instance=product)
        messages.info(request, f'You are editing {product.friendly_name}')

    context = {
        'form': form,
        'product': product,
        'product_type': product_type,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only authorised personnel can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.friendly_name} deleted!')
    return redirect(reverse('products'))
