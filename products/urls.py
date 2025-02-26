from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('books/', views.all_products, name='books'),
    path('accessories/', views.all_products, name='accessories'),
]
