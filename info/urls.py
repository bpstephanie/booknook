from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact-success/', views.contact_success, name='contact_success'),
    path('faqs/', views.faqs, name='faqs'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('partners/', views.partners, name='partners'),
]
