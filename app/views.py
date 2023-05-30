from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from app.models import *
# Create your views here.


def urldata(request,name):
    return HttpResponse(f'hello mr/ms {name}')



class StudentList(ListView):
    template_name='ListsViews.html'
    model=Students
    queryset={'slo':Students}
    

