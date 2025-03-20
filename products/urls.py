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
    path('books/all-genres/', views.all_genres, name='all_genres'),
    path(
        'accessories/all-categories/',
        views.all_categories,
        name='all_categories'
    ),
    path(
        'submit-review/<int:product_id>/',
        views.submit_review,
        name='submit_review'
    ),
    path(
        'review/<int:review_id>/edit/',
        views.edit_review,
        name='edit_review'
    ),
    path(
        'review/<int:review_id>/delete/',
        views.delete_review,
        name='delete_review'
    ),
    path(
        'submit-comment/',
        views.submit_comment,
        name='submit_comment'
    ),
    path(
        'comment/<int:comment_id>/edit/',
        views.edit_comment,
        name='edit_comment'
    ),
    path(
        'comment/<int:comment_id>/delete/',
        views.delete_comment,
        name='delete_comment'
    ),
    path('management/', views.product_management, name='product_management'),
    path('management/add-book/', views.add_book, name='add_book'),
    path(
        'management/add-accessory/',
        views.add_accessory, name='add_accessory'),
    path(
        'management/edit/<int:product_id>/',
        views.edit_product, name='edit_product'),
    path(
        'management/delete/<int:product_id>/',
        views.delete_product, name='delete_product'),
]
