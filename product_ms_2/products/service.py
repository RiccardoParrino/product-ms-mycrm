import json
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

from .models import Product

def findAll():
    products = Product.objects.all()
    products_json = serialize('json', products)
    return HttpResponse(products_json, content_type='application/json')

def update(request):
    name = request.data.get('name')
    p = Product.objects.get(name=name)

    new_name = request.data.get('new_name')
    if new_name is not None:
        p.name = new_name
    
    new_description = request.data.get('new_description')
    if new_description is not None:
        p.description = new_description

    new_unit = request.data.get('new_unit')
    if new_unit is not None:
        p.unit = new_unit
    
    new_price = request.data.get('new_price')
    if new_price is not None:
        p.price = new_price

    new_stock = request.data.get('new_stock')
    if new_stock is not None:
        p.stock = new_stock

    new_notes = request.data.get('new_notes')
    if new_notes is not None:
        p.notes = new_notes

    p.save()

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
    name = request.data.get('name')
    Product.objects.get(name=name).delete()
    return JsonResponse({'msg':'delete endpoint!'})