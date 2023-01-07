from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path("" , views.index , name='home'),
    path('show_my_map', views.show_map, name='show_map'),
    path('choose_path', views.choose, name='choose'),
]