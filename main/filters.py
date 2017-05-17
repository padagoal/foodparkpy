#-*- coding: utf-8 -*-
import django_filters
from main.models import Foodpark


class FoodparkFilter(django_filters.FilterSet):
    nombre_foodpark = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Foodpark
        fields = ['nombre_foodpark']
