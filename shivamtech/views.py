from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from service.models import Service
from news.models import News


def homePage(request):
    servicesData=Service.objects.all()
    return render(request,"amazonclone.html")

def  signin(request):
    try:
        if request.method=="POST":()
        n=int(request.POST.get('user1'))
        print(n)
        
        url="/finalpage/?output={}".format(n)
        return HttpResponseRedirect(url)
    except:
        pass
    return render(request, "signin.html")

def signin(request):
    if request.method=="POST":
        if request.POST.get('user1')=="":
            return render(request,"signin.html",{'error':True})
        n=int(request.POST.get('user1'))
        print(n)
        
        url="/finalpage/?output={}".format(n)
        return HttpResponseRedirect(url)
    return render(request,"signin.html")
        

def finalpage(request):
    newsData=News.objects.all()
    servicesData=Service.objects.all().order_by('-service_title')[2:5]
    
    
    data={
        'servicesData': servicesData,
        'newsData':newsData
    }
    return render(request,"finalpage.html",data)

def newsDetails(request,newsid):
    
    newsDetails=News.objects.get(news_slug=slug)
    data={
        'newsDetails':newsDetails
    }
    return render(request,"newsDetails")




def aboutus(request):
    return render(request,"forms")
def course(request):
    return HttpResponse("welcome to shivamtech 2")



    