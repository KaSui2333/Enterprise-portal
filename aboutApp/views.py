from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Award

# Create your views here.

def survey(request):
    return render(request,'survey.html',{'active_menu':'about',})

def honor(request):
    awards=Award.objects.all()
    return render(request,'honor.html',{
        'active_menu':'about',
        'sub_menu':'honor',
        'awards':awards,
        })