"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view, social_view, services_view
#from products.views import product_detail_view, product_create_view, render_intial_data
from products.views import render_intial_data, dynamic_lookup_view, product_delete_view, product_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('services/', services_view, name='services'),
    path('social/', social_view, name='social'),
    #path('product/detail', product_detail_view, name='pdtDetail'),
    #path('product/create', product_create_view, name='pdtCreate')
    path('product/create/', render_intial_data, name='pdtCreate'),
    path('product/<int:id>/', dynamic_lookup_view, name="pdt"),
    path('product/<int:id>/delete/', product_delete_view, name='pdtDelete'),
    path('products/', product_list_view, name='products')
]
