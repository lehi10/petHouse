from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tienda/404.html')

def error404(request):
    return render(request, 'tienda/404.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')