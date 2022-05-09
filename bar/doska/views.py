from django.shortcuts import render
from .models import notice, comment
from .forms import noticeform

# Create your views here.
def mainpage(request):
    return render(request, "doska/index.html")

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




def noticecreator(request):
    alert=" "
    if request.method == 'POST':
        if noticeform(request.POST).is_valid():
            noticeform(request.POST).save()
            alert = "Сохранено"
        else: alert = "Неккоректные данные"




    noticeData = notice.objects.all()
    commentData = comment.objects.all()

    return render(
    request,
    "doska/noticecreator.html",
    {
    "form": noticeform(),
    "alert": alert
    })

def game(request):
    return render(request,"game/game.html")
