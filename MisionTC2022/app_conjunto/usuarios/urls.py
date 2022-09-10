from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.newTipo_Usuario, name='addTipo_Usuario'),
    path('get', views.getTipo_Usuario, name='getTipo_Usuario'),
]