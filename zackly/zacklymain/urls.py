from django.urls import path, include
from django.shortcuts import render
from django.views import View

from . import views

app_name = 'zacklymain'
urlpatterns = [
    #TOPページ
    path('', views.top.as_view(), name='toppage'),
    #TOP⇒MAINページ、EDITページからのリダイレクト
    path('main/<int:id>/', views.main.as_view(), name='main'),
    #前月に行く用
    path('main/pre/<int:id>/', views.previous.as_view(), name='previous'),
    #次月に行く用
    path('main/for/<int:id>/', views.forward.as_view(), name='forward'),
    path('history/', views.history.as_view(), name='history'),
    #EDITページ
    path('edit/<int:id>/', views.edit.as_view(), name='edit'),
    #新規作成
    path('create/', views.create.as_view(), name='create'),
]
