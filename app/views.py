from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def first_form(request):
     if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('Data is submitted')
     return render(request,'first_form.html')

def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['tn']
        TO=Topic.objects.get_or_create(Topic_name=topic)[0]
        TO.save()
        return HttpResponse('insertion of topic is done')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        topic=request.POST['tn']#to collect data from dictionary        
        TO=Topic.objects.get(Topic_name=topic)#to get data from database


        name=request.POST['name']     
        url=request.POST['url']     

        WO=WebPage.objects.get_or_create(Topic_name=TO,Name=name,Url=url)[0]
        WO.save()


        return HttpResponse('insertion of webpage is done')
    return render(request,'insert_webpage.html',d)

def insert_accessrecords(request):
    if request.method=='POST':
        
        n=request.POST['name']          

        WO=WebPage.objects.get(Name=n)


        date=request.POST['date']
        author=request.POST['author']
        ARO=AccessRecords.objects.get_or_create(Name=WO,Date=date,Author=author)[0]
        ARO.save()


        return HttpResponse('insertion of accessrecords is done')
    return render(request,'insert_accessrecord.html')
 
def retrieve_webpage(request):
     LTO=Topic.objects.all()
     d={'LTO':LTO}
     if request.method=='POST':
         MSTS=request.POST.getlist('topic')#to collect list of objects
         WOS=WebPage.objects.none()#none method for  creating empty queryset
         for i in MSTS:
             WOS=WOS|WebPage.objects.filter(Topic_name=i)
         d1={'WOS':WOS}#submitted data in form of a queryset stored in d1 to send as a context
         return render(request,'display_webpage.html',d1)
     return render(request,'retrieve_webpage.html',d)


def retrieve_accessrecords(request):
    LWO=WebPage.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':#after post method activation
        LMWO=request.POST.getlist('access')#to collect list of multiple objects
        MWO=AccessRecords.objects.none()#none method for  creating empty queryset

        for i in LMWO:
            MWO=MWO|AccessRecords.objects.filter(id=i)#concatenating querysets
        d2={'MWO':MWO}
        return render(request,'display_accessrecords.html',d2)
    return render(request,'retrieve_accessrecords.html',d)
    
def checkbox(request):#creating checkboxes to select multiple data
    LTO=Topic.objects.all()#retrieving all data from backend
    d={'LTO':LTO}#sending data as a context to frontend
    return render(request,'checkbox.html',d)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
















