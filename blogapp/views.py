from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    abouts = About.objects.all()
    return render(request, 'index.html', {'abouts':abouts})


def about_detail(request, pk):
    about = About.objects.get(pk=pk)
    return render(request, 'about_detail.html', {'about':about})





