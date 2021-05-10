from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages


# Create your views here.
 
def index(request):
    return render(request,'index.html')

def about(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc = request.POST.get('desc')
        about = Contact(name=name,email=email,phone=phone,desc=desc)
        about.save()
        messages.success(request, 'Your message has been send!')

    return render(request,'about.html')

def service(request):
    return render(request,'services.html')
