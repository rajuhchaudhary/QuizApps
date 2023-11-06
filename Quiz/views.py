from django.shortcuts import render
from .models import Quiz,Quiz1,Quiz2,Quiz3,Quiz4,Quiz5,Quiz6,Quiz7,Quiz8,Quiz9,Quiz10

# Create your views here.
def demo(request):
    return render(request,'base.html')

def home(request):
    return render(request,'index.html')

def am1(request):
    amazon_data1 = Quiz1.objects.all()
    return render(request,"am1.html",{'d':amazon_data1})

def am2(request):
    amazon_data1 = Quiz2.objects.all()
    return render(request,"am2.html",{'d':amazon_data1})
def am3(request):
    amazon_data1 = Quiz3.objects.all()
    return render(request,"am3.html",{'d':amazon_data1})
def am4(request):
    amazon_data1 = Quiz4.objects.all()
    return render(request,"am4.html",{'d':amazon_data1})
def am5(request):
    amazon_data1 = Quiz5.objects.all()
    return render(request,"am5.html",{'d':amazon_data1})
def am6(request):
    amazon_data1 = Quiz6.objects.all()
    return render(request,"am6.html",{'d':amazon_data1})
def am7(request):
    amazon_data1 = Quiz7.objects.all()
    return render(request,"am7.html",{'d':amazon_data1})
def am8(request):
    amazon_data1 = Quiz8.objects.all()
    return render(request,"am8.html",{'d':amazon_data1})
def am9(request):
    amazon_data1 = Quiz9.objects.all()
    return render(request,"am9.html",{'d':amazon_data1})
def am10(request):
    amazon_data1 = Quiz10.objects.all()
    return render(request,"am10.html",{'d':amazon_data1})
def contact(request):
    return  render(request,'contact.html')