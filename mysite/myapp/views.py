from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category
# Create your views here.
def homePage(request):
    return render(request, 'myapp/index.html')
def contact(request):
    return render(request, 'myapp/contact.html')
def about(request):
    return render(request, 'myapp/about.html')


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'myapp/product_list.html', 
        {'products': products,
         'categories': categories,
    })