from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path(
        'newsletter-signup/',
        views.newsletter_signup, name='newsletter_signup'),
    path(
        'unsubscribe-newsletter/<int:id>/',
        views.unsubscribe_newsletter, name='unsubscribe_newsletter'),
]
