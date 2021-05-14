from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from datetime import datetime


# Create your views here.
 
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        email= request.POST.get('email')
        password= request.POST.get('password')
        gender= request.POST.get('gender')
        phone= request.POST.get('phone') 
        dob= request.POST.get('dob')
        address = request.POST.get('address')
        signup = Contact(name=name,roll=roll,email=email,password=password,gender=gender,phone=phone,dob=dob,address=address)
        signup.save()
        messages.success(request, 'Your message has been send!')

    return render(request,'signup.html')

def service(request):
    return render(request,'services.html')

def signin(request):
    return render(request,'signin.html')
