from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name="forum"),
    path(
        'category/<int:category_id>/create-thread/',
        views.create_thread, name='create_thread'),
    path('add-category/', views.add_category, name='add_category'),
    path(
        'category/<int:category_id>/thread/<int:thread_id>/',
        views.post_list, name='post_list'
    ),
    path(
        'category/<int:category_id>/thread/<int:thread_id>/create-post/',
        views.create_post,
        name='create_post'
    ),
]
