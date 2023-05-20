from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(unit_price__range=(20, 30 ))

    return render(request, 'hello.html', {'name': 'Mazi', 'products': list(queryset)})
    # return HttpResponse('hello boy-boy')

# Create your views here.
