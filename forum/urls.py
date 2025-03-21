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
    path(
        'thread/<int:thread_id>/edit/',
        views.edit_thread, name='edit_thread'),
    path(
        'thread/<int:thread_id>/delete/',
        views.delete_thread, name='delete_thread'),
    path('post/<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete', views.delete_post, name='delete_post'),
]
