from django.shortcuts import render
from .models import *

# Create your views here.

def Indexview(request):
    position = PositionModel.objects.all()
    context = {
        'position':position
    }
    return render(request, 'index.html', context)
