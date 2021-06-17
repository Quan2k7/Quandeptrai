import re
from django.shortcuts import render
from django.http import HttpResponse, response
# Create your views here.
def index(request):
    return HttpResponse("hello may cau")

def ham1(request):
    return HttpResponse("<h1>Xin chao<h1> <p>Hello<p>")