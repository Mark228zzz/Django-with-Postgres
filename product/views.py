from django.shortcuts import render, redirect, get_object_or_404
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

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()

    return redirect('show-products')
