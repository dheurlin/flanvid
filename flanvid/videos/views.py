from django.shortcuts import render, HttpResponse

from .models import Video
from .forms import VideoForm

def index(request):
    vids_list = Video.objects.all()

    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VideoForm()

    return render(request, 'videos/index.html', {
        'vids_list' : vids_list,
        'vid_form'  : form,
    })

def vote(request):
    if request.method == 'POST':
        content = request.POST
    else:
        content = "Empty..."

    return "Hello, Ajax!"
