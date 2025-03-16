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
     path('downloads/', views.downloads, name='downloads'),
     ]
