from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wishlist, WishlistItem
from products.models import Product


# Create your views here.
@login_required
def wishlists(request):
    wishlists = Wishlist.objects.filter(user=request.user).prefetch_related(
        'wishlistitem_set'
    )

    context = {
        'wishlists': wishlists,
    }
    return render(request, "wishlists/wishlist.html", context)


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user_wishlists = Wishlist.objects.filter(user=request.user)

    if request.method == "POST":
        wishlist_id = request.POST.get("wishlist_id")
        new_wishlist_name = request.POST.get("new_wishlist_name")

        # Handle existing or new wishlist
        if wishlist_id:
            wishlist = get_object_or_404(
                Wishlist, id=wishlist_id, user=request.user
            )
        elif new_wishlist_name and new_wishlist_name.strip():
            wishlist, created = Wishlist.objects.get_or_create(
                user=request.user,
                name=new_wishlist_name.strip()
            )
        else:
            messages.error(request, "Please provide a valid wishlist name or select an existing one.")
            return render(request, "products/product_detail.html", {
                "product": product,
                "user_wishlists": user_wishlists,
            })

        # Add product to wishlist
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

    print("User Wishlists:", user_wishlists)  # Debug: Check if wishlists are populated

    return render(request, "products/product_detail.html", {
        "product": product,
        "user_wishlists": user_wishlists,
    })
