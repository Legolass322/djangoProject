from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def test(request, some_argument):
    #test
    return HttpResponse("Hello, world.")

def empty(request):
    #uses when query is empty: product/'nothing'
    return HttpResponse('Choose a product to see more information about it')

def get_product(request, product_id):
    try:
        current_product = Product.objects.filter(id = product_id)
    except Product.DoesNotExist:
        raise Http404("This product does not exist")
    template = loader.get_template('product/get_product.html')
    context = {
        'current_product': current_product,
    }
    return HttpResponse(template.render(context, request))