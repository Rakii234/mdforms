from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    to=TopicForm()
    d={'to':to}
    if request.method=='POST':
        tod=TopicForm(request.POST)
        if tod.is_valid():
            tod.save()
            return HttpResponse('Topic Data Inserted')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    wo = WebpageForm()
    d={'wo': wo}
    if request.method=="POST":
        wod=WebpageForm(request.POST)
        if wod.is_valid():
            wod.save()
            return HttpResponse('Webapge Data Inserted')
    return render(request,'insert_webpage.html',d)

