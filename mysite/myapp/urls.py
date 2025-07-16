from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('products/', views.product_list, name='product_list'),
]
