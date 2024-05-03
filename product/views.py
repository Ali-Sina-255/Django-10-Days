from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import Product


def home(request):
    return HttpResponse('home page')


def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    return HttpResponse(f'product with is this id {product.id}')
