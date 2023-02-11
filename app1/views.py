from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from app1.models import

def home(request):

    # return render(request,"registration.html")
    #   return HttpResponse('hi this is home function')
    return render(request,'aaa/new`.html')


def details(request):
    return render(request,'aaa/registration.html')
    # return HttpResponse('this is details')

def report(request):
     return HttpResponse('this is report function')
    #return render(request,'template/registration.html')
