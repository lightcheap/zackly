from django.urls import path

from . import views

urlpatterns = [
    path('', views.toppage, name='toppage'),
    path('main/', views.main, name='main'),
    path('history/', views.history, name='history'),
    path('edit/', views.edit, name = 'edit'),
]
