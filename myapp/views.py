from django.shortcuts import render
from .models import *

# Create your views here.

def Indexview(request):
    position = PositionModel.objects.all()
    about = AboutModel.objects.all()
    work = ServiceworkModel.objects.all().order_by('id')[:4]
    education = ResumeEducation.objects.all()
    experience = EducationExperience.objects.all().order_by('id')[:4]
    aera = PortfolioAera.objects.all()
    porofolio = Portfolio.objects.all().order_by('id')[:6]
    blogaera = BlogAera.objects.all()
    blog = Blog.objects.all().order_by('id')[:4]
    context = {
        'position':position,
        'about':about,
        'work':work,
        'education':education,
        'experience':experience,
        'aera':aera,
        'porofolio':porofolio,
        'blogaera':blogaera,
        'blog':blog,
    }
    return render(request, 'index.html', context)