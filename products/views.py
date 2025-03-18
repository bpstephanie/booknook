from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, resolve_url
)
from django.contrib.auth.decorators import login_required
from .models import (
    Product, Book, Accessory, Category, Genre, Review, ReviewComment
)
from wishlist.models import Wishlist
from .forms import ReviewForm, ReviewCommentForm, BookForm, AccessoryForm
from django.contrib import messages
from django.http import HttpResponseRedirect
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
        products = Book.objects.all().order_by('name')
        page_title = 'All Books'
    elif product_type == 'accessories':
        products = Accessory.objects.all().order_by('name')
        page_title = 'All Accessories'
    else:
        products = Product.objects.all().order_by('name')
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
    reviews = product.reviews.filter(approved=True)
    user_unnapproved_reviews = (
        product.reviews.filter(approved=False, author=request.user)
        if request.user.is_authenticated else None
    )

    review_count = reviews.count()

    review_form = ReviewForm()
    comment_form = ReviewCommentForm()

    user_wishlists = []
    if request.user.is_authenticated:
        user_wishlists = Wishlist.objects.filter(user=request.user)

    if request.method == "POST":
        if 'review_submit' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.author = request.user
                review.product = product
                review.save()
                return redirect('product_detail', product_id=product.id)
        elif 'comment_submit' in request.POST:
            comment_form = ReviewCommentForm(request.POST)
            if comment_form.is_valid():
                review_id = request.POST.get('review_id')
                review = get_object_or_404(Review, id=review_id)
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.review = review
                comment.save()
                return redirect('product_detail', product_id=product.id)

        paginator = Paginator(reviews, 10)
        page_number = request.GET.get('page', 1)
        reviews = paginator.get_page(page_number)

    context = {
        'product': product,
        'reviews': reviews,
        'review_count': review_count,
        'user_unapproved_reviews': user_unnapproved_reviews,
        'review_form': review_form,
        'comment_form': comment_form,
        'user_wishlists': user_wishlists,
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
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, author=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.approved = False
            review.save()
            messages.success(request, 'Review Updated!')
            return redirect('product_detail', product_id=review.product.id)
        else:
            messages.error(
                request, 'Error updating review!'
            )
    else:
        form = ReviewForm(instace=review)
    return render(request, 'edit_review.html', {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(
        Review, id=review_id, author=request.user
    )
    if request.method == "POST":
        review.delete()
        messages.success(request, 'Review deleted!')
        return redirect('product_detail', product_id=review.product.id)
    else:
        messages.error(
            request, 'You can only delete your own reviews!'
        )
        return HttpResponseRedirect(
            reverse('product_detail', args=[review.product.id])
        )


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(
        ReviewComment, id=comment_id, user=request.user
    )
    if request.method == "POST":
        form = ReviewCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment Updated!')
            return redirect(
                'product_detail', product_id=comment.review.product.id
            )
        else:
            form = ReviewCommentForm(instance=comment)
            messages.error(
                request, 'Error updating comment!'
            )
        return render(request, 'edit_comment.html', {'form': form})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(
        ReviewComment, id=comment_id, author=request.user
    )
    if request.method == "POST":
        comment.delete()
        messages.success(request, 'Comment deleted!')
        return redirect('product_detail', product_id=comment.review.product.id)
    else:
        messages.error(
            request, 'You can only delete your own comments!'
        )
    return HttpResponseRedirect(
        reverse('product_detail', args=[comment.review.product.id])
    )


def product_management(request):
    """ Displays product management page """
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


def add_book(request):
    """ Add a book to the store """
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added book!')
            return redirect(
                resolve_url('product_management') + '?section=addBook')
        else:
            messages.error(
                request, (
                    'Failed to add book. Please ensure the form is valid.'
                ))
    else:
        form = BookForm()
    return redirect('product_management')


def add_accessory(request):
    """ Add an accessory to the store """
    if request.method == 'POST':
        form = AccessoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added accessory!')
            return redirect(
                resolve_url('product_management') + '?section=addAccessory')
        else:
            messages.error(
                request, (
                    'Failed to add accessory. Please ensure the form is valid.'
                ))
    else:
        form = AccessoryForm()
    return redirect('product_management')


def edit_book(request, book_id):
    """ Edit a book in the store """
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Successfully updated {book.friendly_name}!')
            return redirect('product_detail', product_id=book.id)
        else:
            messages.error(
                request,
                (
                    f'Failed to update {book.friendly_name}. '
                    'Please ensure the form is valid.'
                ))
    else:
        form = BookForm(instance=book)
        messages.info(request, f'You are editing {book.friendly_name}')

    book_form = form

    template = 'products/edit_book.html'
    context = {
        'book_form': book_form,
        'book': book,
    }

    return render(request, template, context)
