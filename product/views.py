from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'product.html', context=context)
