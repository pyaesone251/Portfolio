from django.shortcuts import render
from .models import *

# Create your views here.

def Indexview(request):
    position = PositionModel.objects.all()
    about = AboutModel.objects.all()
    work = ServiceworkModel.objects.all().order_by('id')[:4]

    context = {
        'position':position,
        'about':about,
        'work':work,
    }
    return render(request, 'index.html', context)