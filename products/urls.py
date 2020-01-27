from django.urls import path

from .views import render_intial_data, dynamic_lookup_view, product_delete_view, product_list_view


app_name = 'products'
urlpatterns = [
    #path('product/detail', product_detail_view, name='pdtDetail'),
    #path('product/create', product_create_view, name='pdtCreate')
    path('create/', render_intial_data, name='pdtCreate'),
    path('<int:id>/', dynamic_lookup_view, name="pdt"),
    path('<int:id>/delete/', product_delete_view, name='pdtDelete'),
    path('', product_list_view, name='products')
]
