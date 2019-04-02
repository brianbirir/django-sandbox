from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'hi_there': 'This is Brian'})


def eggs(request):
    return HttpResponse('Eggs are tasty when scrambled')


def count(request):
    return render(request, 'count.html')
    