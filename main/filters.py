# -*- coding: utf-8 -*-
import django_filters
from main.models import Foodpark
from main.models import Local


class FoodparkFilter(django_filters.FilterSet):
    nombre_foodpark = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Foodpark
        fields = ['nombre_foodpark']


class LocalFilter(django_filters.FilterSet):
    nombre_local = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Local
        fields = ['nombre_local']
