from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")

def empty(request):
    return HttpResponse('Choose a product to see more information about it')