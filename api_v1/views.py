from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os


# Create your views here.


def home_page(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    myskills = Projects.objects.all()
    skills = Skills.objects.all()
    context = {
        "info": myinfo,
        "about": myabout,
        "skills": myskills,
        "know": skills
    }

    return render(request, 'home.html', context)

def loginpage(request):
    return render(request, 'login.html')

def resume(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    myskills = Projects.objects.all()
    skills = Skills.objects.all()
    context = {
        "info": myinfo,
        "about": myabout,
        "skills": myskills,
        "know": skills
    }
    return render(request, 'resume.html', context)


import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse


def download_pdf(request):
    filename = "AZAD_KHAN.pdf"
    filepath = os.getcwd() +'/media/cv/'+ filename
    path = open(filepath, 'rb')
    response = HttpResponse(path, content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response