from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def product(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'products.html', context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-products')
    else:
        form = ProductForm()

    context = {'form': form}

    return render(request, 'product_form.html', context)
