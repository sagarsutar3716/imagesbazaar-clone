from django.shortcuts import render,HttpResponse
from .models import *


def home(request):
  cats = Categorie.objects.all()
  images = Image.objects.all()

  context = {'images':images, 'cats':cats}

  return render (request, 'imagesbazaars/home.html', context)


def category(request, cid):
  cats = Categorie.objects.all()
  category = Categorie.objects.get(pk=cid)
  images = Image.objects.filter(cat=category)

  context = {'images':images, 'cats':cats, 'category':category}

  return render (request, 'imagesbazaars/home.html', context)


def search(request):
  query = request.GET['query']
  if len(query)>50:
    images = []
  else:     
    images = Image.objects.filter(title__icontains=query)
  context = {'images':images, 'query':query}
  return render(request,'imagesbazaars/search.html',context)