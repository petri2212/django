# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  #  return HttpResponse("Hello World! im petri")
  return render(request, 'home.php')

def about(request):
  #  return HttpResponse("Sei in about")
  return render(request, 'about.php')