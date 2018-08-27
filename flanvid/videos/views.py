from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Hello, world! This is the videos index!")
