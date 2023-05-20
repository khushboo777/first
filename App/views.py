from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def FBV(request):
    return HttpResponse("<marquee right><h1>This is for practice only...<marquee right><h1>")

def mihir(request):
    return HttpResponse("<h1><marquee>i am here </h1></marquee>")