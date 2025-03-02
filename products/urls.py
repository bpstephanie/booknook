from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path(
        'books/',
        views.all_products,
        name='all_books',
        kwargs={'type': 'books'}
    ),
    path(
        'accessories/',
        views.all_products,
        name='all_accessories',
        kwargs={'type': 'accessories'}
    ),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('books/all-genres', views.all_genres, name='all_genres'),
]
