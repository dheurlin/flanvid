from django.shortcuts import render, HttpResponse

from .models import Video

def index(request):
    return render(request, 'videos/index.html', {
        'vids_list' : Video.objects.all(),
    })
