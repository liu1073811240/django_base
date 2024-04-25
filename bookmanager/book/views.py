from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# **views.py**文件用于编写Web应用视图。
def index(request):
    return HttpResponse("OK")
