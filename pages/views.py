from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from products.models import Product


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    #products= Product.objects.all()
    context = {
        "my_text": "This is about us",
        "my_items": ['sauce', 'more sauce', 'even more sauce', 122]
    }
    # return HttpResponse("<h1>About Page</h1>")
    return render(request, "about.html", context)


def services_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Services Page</h1>")
    return render(request, "services.html", {})


def social_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Social Page</h1>")
    return render(request, "social.html", {})
