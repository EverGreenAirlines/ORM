from django.shortcuts import render,HttpResponse
from django.urls import reverse

# Create your views here.

def hello(request):
    import datetime
    now=datetime.datetime.now()
    return render(request,'helloworld.html',{'edate':now})

def login(request):
    return render(request,'login.html')

def runoob(request):
    context = {}
    context['cainiao'] = 'www.runoob.com'
    context['baidu'] = "www.baidu.com"
    context['jingdong'] = "www.jd.com"
    return render(request, 'runoob.html', {'context':context})

def index(request):

    return HttpResponse('app01.index')
    # return HttpResponse(reverse('app01:index'))