import os
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,"index.html")

def addmissionform(request):
    return render(request, "addmissionform.html")

def signup_page(request):
    return render(request, "signup_page.html")

def syllabus(request):
    return render(request, "syllabus.html")

def teacher_login(request):
    return render(request, "teacher_login.html")

def result_main(request):
    return render(request, "result_main.html")

def result_rollno(request):
    return render(request, "result_rollno.html")

def aboutus(request):
    return render(request, "aboutus.html")

def c_us(request):
    return render(request, "c_us.html")



# def signupdata(request):

#     if request.method=="POST":
#         email=request.POST.get('email')
#         password=request.POST.get('password')

#         s_data=signupdata(email=email,password=password)
#         s_data.save()

#     return render(request,"signup_page.html")

