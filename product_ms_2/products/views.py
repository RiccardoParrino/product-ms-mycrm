from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def findAll(request):
    return JsonResponse({'msg':'findAll endpoint!'})

def update(request):
    return JsonResponse({'msg':'update endpoint!'})

def create (request):
    return JsonResponse({'msg':'create endpoint!'})

def delete (request):
    return JsonResponse({'msg':'delete endpoint!'})