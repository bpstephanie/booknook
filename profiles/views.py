from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile, PDF
from checkout.models import Order
from wishlist.models import Wishlist, WishlistItem
from forum.models import Category, Thread, Post
from home.models import NewsletterSignup
from products.models import Review

from bag.contexts import bag_contents

from .forms import DeliveryDetailsForm, PersonalInfoForm
from forum.forms import ThreadForm
from home.forms import NewsletterSignupForm
from products.forms import ReviewForm


# Create your views here.
@login_required
def profile(request):
    """
    Display user's profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    delivery_form = DeliveryDetailsForm(instance=profile)
    personal_info_form = PersonalInfoForm(instance=profile)
    orders = profile.orders.all()
    wishlists = Wishlist.objects.filter(user=request.user)
    saved_items = bag_contents(request)['saved_items']
    threads = Thread.objects.filter(created_by=request.user, is_deleted=False)
    categories = Category.objects.all()
    reviews = Review.objects.filter(author=request.user).select_related(
        'product'
    )
    review_form = ReviewForm()
    newsletter_form = NewsletterSignupForm(instance=profile)
    newsletter_signup = NewsletterSignup.objects.filter(
        email=request.user.email
    ).first()

    # Filter categories
    categories_with_threads = [
        category for category in categories
        if threads.filter(category=category).exists()
    ]

    section = request.GET.get('section', 'deliveryDetails')

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'delivery_form': delivery_form,
        'personal_info_form': personal_info_form,
        'orders': orders,
        'wishlists': wishlists,
        'saved_items': saved_items,
        'threads': threads,
        'categories': categories_with_threads,
        'section': section,
        'on_profile_page': True,
        'newsletter_form': newsletter_form,
        'newsletter_signup': newsletter_signup,
        'reviews': reviews,
        'review_form': review_form,
    }
    return render(request, template, context)


@login_required
def update_delivery_details(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = DeliveryDetailsForm(
            request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Delivery details updated successfully')
            return redirect(
                resolve_url('profile') + '?section=deliveryDetails')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = DeliveryDetailsForm()
    return redirect('profile')


@login_required
def update_personal_info(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal info updated successfully')
            return redirect(resolve_url('profile') + '?section=personalInfo')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = PersonalInfoForm()
    return redirect('profile')


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def downloads(request):
    pdfs = PDF.objects.all()
    template = 'profiles/downloads.html'

    return render(request, template, {'pdfs': pdfs})


@login_required
def remove_wishlist_item(request, item_id):
    item = get_object_or_404(WishlistItem, id=item_id)

    if item.wishlist.user == request.user:
        item.delete()
        messages.success(request, 'Wishlist item deleted!')
    else:
        messages.error(
            request, 'Something went wrong - your item was not deleted.')
    return redirect(resolve_url('profile') + '?section=myWishlists')


@login_required
def remove_wishlist(request, wishlist_id):
    wishlist = get_object_or_404(Wishlist, id=wishlist_id)

    if wishlist.user == request.user:
        wishlist.delete()
        messages.success(request, 'Wishlist deleted!')
    else:
        messages.error(
            request, 'Something went wrong - your wishlist was not deleted.')
    return redirect(resolve_url('profile') + '?section=myWishlists')


@login_required
def edit_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)

    if request.user != thread.created_by:
        messages.error(request, 'You are not authorized to edit this thread.')
        return redirect('profile')

    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thread updated successfully!')
            return redirect(
                resolve_url('profile') + '?section=forumInteraction')
        else:
            messages.error(
                request, 'Updated failed. Please ensure the form is valid.')
    else:
        form = ThreadForm(instance=thread)

    template = 'forum/edit_thread.html'
    context = {
        'form': form,
        'thread': thread,
    }
    return render(request, template, context)


@login_required
def delete_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)

    if request.user != thread.created_by:
        messages.error(
            request,
            'You are not authorized to delete this thread.')
        return redirect('profile')

    thread.is_deleted = True
    thread.save()
    messages.success(request, 'Thread deleted successfully!')
    return redirect(resolve_url('profile') + '?section=forumInteraction')


@login_required
def update_review(request):
    review_id = request.POST.get('review_id')
    review = get_object_or_404(Review, id=review_id, author=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.approved = False
            review.save()
            messages.success(request, 'Review updated successfully!')
            return redirect(resolve_url('profile') + '?section=userReviews')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
    return redirect('profile')
