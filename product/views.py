from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Product


def test(request, product_id):
    current_product = get_object_or_404(Product, pk = product_id)
    return render(request, "product/get_product.html", 
        {'current_product': current_product})

def empty(request):
    #uses when query is empty: product/'nothing'
    return HttpResponse('Choose a product to see more information about it')

def get_product(request, product_id):
    current_product = get_object_or_404(Product, pk = product_id)
    return render(request, "product/get_product.html", 
        {'current_product': current_product})