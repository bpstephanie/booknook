from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlists, name="wishlists"),
    path(
        'add/<int:product_id>/',
        views.add_to_wishlist,
        name='add_to_wishlist'
    ),
]
