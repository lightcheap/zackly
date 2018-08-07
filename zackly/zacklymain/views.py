from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def toppage(request):
    #template = loader.get_template('zacklymain/toppage.html')
    return render(request,'zacklymain/toppage.html')

def main(request):
    #template = loader.get_template('zacklymain/main.html')
    return render(request,'zacklymain/main.html')

def history(request):
    #template = loader.get_template('zacklymain/history.html')
    return render(request,'zacklymain/history.html')

def edit(request):
    return render(request,'zacklymain/edit.html')