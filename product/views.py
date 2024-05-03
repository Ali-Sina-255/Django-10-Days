from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product


def bad_view(request, *args, **kwargs):
    # print(dict(request.GET))
    new_request_data = dict(request.GET)
    new_product = new_request_data.get('new_product')
    print(new_request_data, new_product)
    if new_product[0].lower() == 'true':
        print("new product")
        Product.objects.create(title=new_request_data.get('title')[0], content=new_request_data.get('content')[0])
    return HttpResponse("dont this")


def product_create(request, *args, **kwargs):
    context = {}
    return render(request, 'form.html', context)


def home(request):
    return HttpResponse('home page')


def product_list(request):
    qs = Product.objects.all()
    context = {
        "products": qs
    }
    return render(request, 'product/product_list.html', context)


def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    return render(request, 'product/detail.html')
