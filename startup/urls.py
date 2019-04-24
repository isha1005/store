from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='startup-home'),
    path('about/', views.about, name='startup-about'),
    path('contact/', views.contact, name='startup-contact'),
    path('faq/', views.faq, name='startup-faq'),
    path('plan/', views.plan, name='startup-plan'),
    path('amenities', views.amenities, name='startup-amenities'),
]
