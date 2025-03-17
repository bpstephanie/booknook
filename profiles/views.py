from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile, PDF
from checkout.models import Order
from wishlist.models import Wishlist
from bag.models import SavedItem
from forum.models import Category, Thread, Post

from bag.contexts import bag_contents

from .forms import DeliveryDetailsForm, PersonalInfoForm


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
    threads = Thread.objects.filter(created_by=request.user)
    categories = Category.objects.all()

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
        'categories': categories,
        'section': section,
        'on_profile_page': True,
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
            return redirect('profile')
    return redirect('profile')


@login_required
def update_personal_info(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal info updated successfully')
            return redirect('profile')
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
