from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('А вот и главная страница')


def group_post(request, slug):
    return HttpResponse(f'Познакомьтесь, это группа {slug}')
