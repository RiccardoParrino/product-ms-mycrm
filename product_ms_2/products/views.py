from django.shortcuts import render
from django.http import JsonResponse

from . import service

# Create your views here.

def findAll(request):
    return service.findAll(request)

def update(request):
    return service.update(request)

def create (request):
    return service.create(request)

def delete (request):
    return service.delete(request)