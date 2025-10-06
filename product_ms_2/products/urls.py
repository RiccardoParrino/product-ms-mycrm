from django.urls import path
from . import views

urlpatterns = [
    path('findAll/', views.findAll, name='findAll'),
    path('delete/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update')
]