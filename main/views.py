#-*- coding: utf-8 -*-
from django.shortcuts import render

from main import models
from main.filters import FoodparkFilter
from main.filters import LocalFilter
from main.models import Foodpark
from main.models import Local


def IndexView(request):
    foodparks = models.Foodpark.objects.all()
    ciudad = 'Asunción'
    context = {
        'ciudad': ciudad,
        'foodparks':foodparks
    }
    return render(request, 'main/index.html',context)

def foodparksView(request):
    filter = FoodparkFilter(request.GET, queryset=Foodpark.objects.all())
    foodparks = models.Foodpark.objects.all()
    ciudad = 'Asunción'
    context = {
        'filter': filter,
        'ciudad': ciudad,
        'foodparks':foodparks
    }
    return render(request, 'main/foodparks.html',context)

def localesView(request):
    filter = LocalFilter(request.GET, queryset=Local.objects.all())
    locales = models.Local.objects.all()
    context = {
        'filter': filter,
        'locales': locales
    }
    return render(request, 'main/locales.html',context)