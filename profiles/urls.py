from django.urls import path
from . import views

urlpatterns = [
     path('', views.profile, name='profile'),
     path('update_delivery_details/',
          views.update_delivery_details,
          name='update_delivery_details'),
     path('update_personal_info/',
          views.update_personal_info,
          name='update_personal_info'),
     path(
          'order_history/<str:order_number>',
          views.order_history, name='order_history'),
     path(
         'remove_wishlist_item/<int:item_id>/',
         views.remove_wishlist_item, name='remove_wishlist_item'),
     path(
         'remove_wishlist/<int:wishlist_id>/',
         views.remove_wishlist, name='remove_wishlist'),
     path('downloads/', views.downloads, name='downloads'),
     ]
