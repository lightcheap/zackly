from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def toppage(request):
    return HttpResponse("トップページです。")

def main(request):
    return HttpResponse("メインページです。")

def history(request):
    return HttpResponse("履歴ページです。")