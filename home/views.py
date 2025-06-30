from django.shortcuts import render
from catalog.models import Product

def home(request):
    products = Product.objects.filter(is_hit=True)
    return render(request, "home.html", context={"products": products})