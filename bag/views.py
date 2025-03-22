from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import SavedItem
from products.models import Product


# Create your views here.
def view_bag(request):
    """ A view that renders the bag contents page """
    saved_items = []
    if request.user.is_authenticated:
        saved_items = SavedItem.objects.filter(user=request.user)

    context = {
        'saved_items': saved_items,
    }
    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ A view to add a quantity of a specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request,
            f'Updated {product.friendly_name} quantity to {bag[item_id]}'
        )
    else:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Added {product.friendly_name} to you bag'
        )

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of a specified product to the specified quantity"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {product.friendly_name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(
            request,
            f'Removed {product.friendly_name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ View to remove the item from the shopping bag """
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(
            request,
            f'Removed {product.friendly_name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


@login_required
def save_for_later(request, item_id):
    """ Save an item for later """
    if not request.user.is_authenticated:
        messages.info(
            request,
            'Please log in to save items for later'
        )
        return redirect(reverse('account_login'))

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            quantity = bag.pop(item_id)
            saved_item, created = SavedItem.objects.get_or_create(
                user=request.user,
                product=product,
                quantity=quantity
            )
            if created:
                saved_item.quantity = quantity
            else:
                saved_item.quantity += quantity
            saved_item.save()
            messages.success(
                request,
                f'Saved {product.friendly_name} for later'
            )
            request.session['bag'] = bag
        else:
            saved_item, created = SavedItem.objects.get_or_create(
                user=request.user,
                product=product,
            )
            if created:
                saved_item.quantity = 1
                saved_item.save()
                messages.success(
                    request,
                    f'Saved {product.friendly_name} for later'
                )
    except Exception as e:
        messages.error(request, f'Error saving item: {e}')
    return redirect(reverse('view_bag'))


@login_required
def move_to_bag(request, item_id):
    """ Move a saved item back to the bag """

    saved_item = get_object_or_404(SavedItem, pk=item_id, user=request.user)
    product_id = saved_item.product.id
    bag = request.session.get('bag', {})

    if product_id in bag:
        bag[product_id] += saved_item.quantity
    else:
        bag[product_id] = saved_item.quantity

    saved_item.delete()
    request.session['bag'] = bag
    messages.success(
        request,
        f'Moved {saved_item.product.friendly_name} back to you bag'
    )
    return redirect(reverse('view_bag'))


@login_required
def remove_saved_item(request, item_id):
    """ Remove a saved item from the saved items list """

    saved_item = get_object_or_404(SavedItem, pk=item_id, user=request.user)
    saved_item.delete()
    messages.success(
        request,
        f'Removed {saved_item.product.friendly_name} from your saved items'
    )
    return redirect(reverse('view_bag'))


@login_required
def adjust_saved_item(request, item_id):
    """Adjust the quantity of a saved item"""
    saved_item = get_object_or_404(SavedItem, pk=item_id, user=request.user)
    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        saved_item.quantity = quantity
        saved_item.save()
        messages.success(
            request,
            (
                f'Updated {saved_item.product.friendly_name} quantity to '
                f'{saved_item.quantity}'
            )
        )
    else:
        saved_item.delete()
        messages.success(
            request,
            f'Removed {saved_item.product.friendly_name} from your saved items'
        )
    next_url = request.POST.get('next', reverse('view_bag'))
    return redirect(next_url)
