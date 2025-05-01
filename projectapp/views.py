import os
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,"index.html")

def addmissionform(request):
    return render(request, "addmissionform.html")

def signup_page(request):
    return render(request, "signup_page.html")

# def signupdata(request):

#     if request.method=="POST":
#         email=request.POST.get('email')
#         password=request.POST.get('password')

#         s_data=signupdata(email=email,password=password)
#         s_data.save()

#     return render(request,"signup_page.html")

def my_website(request):
    return render(request, "my_website.html")
