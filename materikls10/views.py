from django.shortcuts import render
from django.template import loader 
from django.http import HttpResponse


# Create your views here.
def index(request): 
    template = loader.get_template('index.html') 
    return render (request, 'index.html')

def peluang(request):
    template = loader.get_template('peluang.html')
    return HttpResponse(template.render())

def BarisandanDeret(request):
    template = loader.get_template('BarisandanDeret.html')
    return render (request, 'BarisandanDeret.html')

def Eksponen(request):
    template = loader.get_template('Eksponen.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return render(request,'home.html')


def Referensi(request):
    template = loader.get_template('Referensi.html')
    return HttpResponse(template.render())

def Statistika(request):
    template = loader.get_template('Statistika.html')
    return HttpResponse(template.render())

def LogOut(request):
    template = loader.get_template('LogOut.html')
    return render(request,'index.html')