from django.shortcuts import render
from .models import notice, comment

# Create your views here.

def doska(request):
    noticeData = notice.objects.all()
    commentData = comment.objects.all()
    return render(
    request,
    "doska/doska.html",
    {
    "notice": noticeData ,
    "comment": commentData
    })

def mainpage(request):
    return render(request, "doska/index.html")

def game(request):
    return render(request,"game/game.html")
