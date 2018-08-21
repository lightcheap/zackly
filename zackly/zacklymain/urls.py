from django.urls import path
from django.shortcuts import render
from django.views import View

from . import views
app_name = 'zacklymain'
urlpatterns = [
    path('', views.top.as_view(), name='toppage'),
    path('main/', views.main.as_view(), name='main'),
    path('history/', views.history.as_view(), name='history'),
    path('edit/', views.edit.as_view(), name = 'edit'),
    path('create/', views.edit.as_view(), name = 'create')
]
