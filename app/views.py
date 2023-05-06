from django.http import HttpResponse
import datetime
import os
from django.shortcuts import render, reverse

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)
    

def time_view(request):
    return HttpResponse(f'Time = {datetime.datetime.now().time()}')

def workdir_view(request):
    res = ''
    list_ = os.listdir(path='.')
    for i in list_:
        res += f'<div>{i}</div>'
    return HttpResponse(res)

