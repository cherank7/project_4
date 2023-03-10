from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def kohli(request):
    return HttpResponse('Kohli is the best batsman')

def abd(request):
    return HttpResponse('abd is a Mr.360')

def fans(request):
    return HttpResponse('<h1><marquee>Rcbians:- esaala cup naamdhe</h1></marquee><h2><marquee>others:-maaaku nammakam ledhu dhora</h2></marquee>')