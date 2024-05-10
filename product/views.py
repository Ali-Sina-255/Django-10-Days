from django.shortcuts import render, redirect

from django.http import HttpResponse, Http404
from .models import Product
from django.contrib.admin.views.decorators import staff_member_required
from . forms import ProductForm


def bad_view(request, *args, **kwargs):
    # print(dict(request.GET))
    new_request_data = dict(request.GET)
    new_product = new_request_data.get('new_product')
    print(new_request_data, new_product)
    if new_product[0].lower() == 'true':
        print("new product")
        Product.objects.create(title=new_request_data.get('title')[0], content=new_request_data.get('content')[0])
    return HttpResponse("dont this")

@staff_member_required
def product_create(request, *args, **kwargs):
    if request.method == 'POST': 
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form =ProductForm()
    context = {}
    return render(request, 'form.html', context)


def home(request):
    return render(request, 'product/home.html')


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
