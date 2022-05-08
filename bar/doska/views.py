from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def doska(request):
    return HttpResponse("Its doska")

def mainpage(request):
    return HttpResponse("Its a mainpage")

def game(request):
    return render(request,"game/game.html")
