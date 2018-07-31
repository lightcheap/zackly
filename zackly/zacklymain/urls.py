from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('top/', views.toppage, name='toppage'),
    path('history/', views.history, name='history'),
]
