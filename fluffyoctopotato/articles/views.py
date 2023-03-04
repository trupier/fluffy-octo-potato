from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #no context
    return render(request, 'home.html')