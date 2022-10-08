from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio',views.inicio, name='inicio'),
    path('ingresar',views.ingresar, name='ingresar'),
    path('registrar',views.registrar, name='registrar'),
]