from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template) 

# def index(request):
#     return HttpResponse('А вот и главная страница')


def group_post(request, slug):
    return HttpResponse(f'Познакомьтесь, это группа {slug}')
