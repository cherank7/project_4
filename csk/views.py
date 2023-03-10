from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dhoni(request):
    return HttpResponse('<h1><marquee>MSD is the greatest finisher</h1><marquee>')


def raina(request):
    return HttpResponse('<h1>Raina is known as Mr.IPL')

def jadeja(request):
    return HttpResponse('<h2>Sir Jadeja</h2')