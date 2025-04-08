from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')


def place(request):
    return render(request, 'place.html')