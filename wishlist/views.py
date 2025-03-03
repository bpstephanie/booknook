from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wishlist, WishlistItem
from products.models import Product


# Create your views here.
@login_required
def wishlists(request):
    wishlists = Wishlist.objects.filter(user=request.user)

    context = {
        'wishlists': wishlists,
    }
    return render(request, "wishlists/wishlists.html", context)


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        wishlist_id = request.POST.get("wishlist_id")
        new_wishlist_name = request.POST.get("new_wishlist_name")

        # If user selects an existing wishlist
        if wishlist_id:
            wishlist = get_object_or_404(
                Wishlist, id=wishlist_id, user=request.user
            )
        # If user creates a new wishlist
        elif new_wishlist_name:
            wishlist = Wishlist.objects.create(
                user=request.user, name=new_wishlist_name
            )
        else:
            messages.error(request, "No valid wishlist selected or created.")
            return redirect("product_detail", product_id=product.id)

        # If item isn't already in wishlist
        if not WishlistItem.objects.filter(
            wishlist=wishlist, product=product
        ).exists():
            WishlistItem.objects.create(wishlist=wishlist, product=product)
            messages.success(
                request, f"'{product.name}' has been added to {wishlist.name}"
            )
        else:
            messages.warning(
                request, f"'{product.name}' already exists in {wishlist.name}"
            )
            return redirect("product_detail", product_id=product.id)

    user_wishlists = Wishlist.objects.filter(user=request.user)

    return render(request, "wishlist/add_to_wishlist.html", {
        "product": product,
        "user_wishlists": user_wishlists,
    })
