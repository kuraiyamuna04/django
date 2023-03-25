from django.shortcuts import render
from app import models 
from app.models import Sign_up
from app.models import Contact_data
from app.models import Subscribe
from app.models import Application




# Create your views here.

def index(request):
    return render(request,"index.html")

def subscribed(request):
     if request.method =="POST":
        e_mail = request.POST.get('e_mail')
        subscribe = Subscribe(e_mail=e_mail)
        subscribe.save()
     return render(request,"subscribed.html")

def jobs(request):
    return render(request,"jobs.html")

def digitalmarketer(request):
    return render(request,"digitalmarketer.html")

def wordpress(request):
    return render(request,"wordpress.html")

def visual(request):
    return render(request,"visual.html")

def creative(request):
    return render(request,"creative.html")


def candidate(request):
    return render(request,"candidate.html")

def jobdetails(request):
    return render(request,"job_details.html")

def application(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        link = request.POST.get('link')
        CV = request.POST.get('CV')
        coverletter = request.POST.get('coverletter')
        application = Application( fullname= fullname,  email= email,link= link ,CV = CV, coverletter=coverletter)
        application.save()
    return render(request,"applicationDone.html")

def element(request):
    return render(request,"elements.html")

def blog(request):
    return render(request,"blog.html")

def singleblog(request):
    return render(request,"single-blog.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    return render(request,"login.html")

def aftersignUp(request):
     if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        sign_up = Sign_up( firstname= firstname, lastname= lastname, email= email,password=password)
        sign_up.save()
     return render(request,"aftersignUp.html")

def resume(request):
    return render(request,"resume.html")

def signup(request):
    return render(request,"sign_up.html")

def aftercontact(request):
 if request.method == "POST":
        message = request.POST.get('message')
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        subject = request.POST.get('subject')
        contact_data = Contact_data(  message = message,name = name, mail= mail,subject = subject )
        contact_data.save()
 return render(request,"aftercontact.html")