
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from products.models import Product
from products.forms import ProductForm, RawProductForm
# Create your views here.

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../../')
    context = {
        "obj": obj
    }
    return render(request, "products/product_delete.html", context)


def render_intial_data(request):
    initial_data = {
        'title': "my awesome title",
    }
    form = RawProductForm(request.POST or None, initial=initial_data)
    context = {
        "form": form,
    }
    return render(request, "products/product_create.html", context)


def dynamic_lookup_view(request, id):
    #obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # try:
    #    obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #    raise Http404

    context = {
        "obj": obj
    }
    return render(request, "products/product_detail.html", context)


"""
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #    "title": obj.title,
    #    "description": obj.description,
    #    "price": obj.price
    # }
    context = {
        "obj": obj
    }
    return render(request, "products/product_detail.html", context)
"""

"""
def product_create_view(request):
    my_form = RawProductForm(request.POST)
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)


"""

"""
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form,
    }
    return render(request, "products/product_create.html", context)
"""
