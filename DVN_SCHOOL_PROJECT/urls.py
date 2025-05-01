"""
URL configuration for DVN_SCHOOL_PROJECT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projectapp import views
# from projectapp.models import signupdata

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('addmissionform/', views.addmissionform, name="addmissionform"),
    path('signup/', views.signup_page, name='signup'),
    # path('signpData/', views.signupdata, name="signpData"),
    path('mywebsite/', views.my_website, name='mywebsite'),
]
