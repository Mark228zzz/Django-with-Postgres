from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='show-products'),
    path('add-product/', views.create_product, name='add-product'),
]
