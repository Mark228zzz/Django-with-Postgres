from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='show-products'),
    path('add-product/', views.create_product, name='add-product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete-product')
]
