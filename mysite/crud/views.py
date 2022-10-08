from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """ return render(request, 'index.html') """
    """ return HttpResponse(":DD") """
    return render(request, 'paginas/inicio.html')
def inicio(request):
    return render(request, 'paginas/inicio.html')
def ingresar(request):
    return render(request, 'registros/ingresar.html')
def registrar(request):
    return render(request, 'registros/registrar.html')
# Create your views here.
