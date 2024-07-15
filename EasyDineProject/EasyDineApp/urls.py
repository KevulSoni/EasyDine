from django.contrib import admin
from django.urls import path
from . import views
from .views import rest_list
from .views import booktable, paymentInvoice

urlpatterns = [
    path("", views.login_view, name='login'),
    path('signup.html', views.signup_view, name='signup'),
    path("index.html", views.home, name='home'),
    path("about.html", views.about, name='about'),
    path("contact.html", views.contact, name='contact'),
    path("booking.html", views.booking, name='booking'),
    path("service.html", views.service, name='service'),
    path('restaurants/', rest_list, name='rest_list'),
    path('payment.html', views.payment, name='payment'),
    path('restList.html', views.rest_list, name='rest_list'),
    path('restDetails.html', views.restDetails, name='restDetails'),
    path('restaurantDetails/<int:restaurant_id>/', views.restaurantDetails, name='restaurantDetails'),
    path("booktable", views.booktable, name='booktable'),
    path("paymentInvoice/<int:booking_id><int:restaurant_id>/", views.paymentInvoice, name='paymentInvoice'),

    path('paymentSuccess.html', views.paymentSuccess, name='paymentSuccess'),
  
]

