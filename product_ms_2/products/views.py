from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

from . import service

# Create your views here.

@api_view(['GET'])
def findAll(request):
    return service.findAll(request)

@api_view(['PATCH'])
def update(request):
    return service.update(request)

@api_view(['POST'])
def create (request):
    print(request.data.get('name'))
    print(request.data.get('description'))
    return service.create(request)

@api_view(['DELETE'])
def delete (request):
    return service.delete(request)