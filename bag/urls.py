from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('save_for_later/<item_id>/',
         views.save_for_later, name='save_for_later'),
    path('move_to_bag/<int:item_id>/', views.move_to_bag, name='move_to_bag'),
    path('remove_saved_item/<item_id>/', views.remove_saved_item,
         name='remove_saved_item'),
]
