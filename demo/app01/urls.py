from django.contrib import admin
from django.urls import path,re_path,include
from app01 import views

urlpatterns = [

    re_path('index/',views.index,name='index'),

]