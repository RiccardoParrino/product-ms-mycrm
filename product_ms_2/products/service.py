from django.http import JsonResponse

from .models import Product


def findAll(request):
    return JsonResponse({'msg':'findAll endpoint!'})

def update(request):
    return JsonResponse({'msg':'update endpoint!'})

def create (request):
    name = request.data.get('name')
    description = request.data.get('description')
    unit = request.data.get('unit')
    price = request.data.get('price')
    stock = request.data.get('stock')
    notes = request.data.get('notes')
    product = Product(
        name=name, 
        description=description,
        unit=unit,
        price=price,
        stock=stock,
        notes=notes
    )
    product.save()
    return JsonResponse({'msg':'product inserted!'})

def delete (request):
    return JsonResponse({'msg':'delete endpoint!'})