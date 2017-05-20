from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'foodparks/', views.foodparksView, name='foodparks'),
    url(r'locales/', views.localesView, name='locales')
]