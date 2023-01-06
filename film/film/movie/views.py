from django.shortcuts import render
from django.http import HttpResponse
from . models import movie

# Create your views here.

def index(request):
    a=movie.objects.all()
    return render(request,'index.html',{'b':a})

def detail(request,movie_id):
    g=movie.objects.filter(id=movie_id)
    return render(request,'detail.html',{'h':g})