from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db import transaction

from django_ajax.decorators import ajax

from .models import Video
from .forms import VideoForm

def index(request):
    vids_list = Video.objects.all().order_by('-points')

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

@ajax
def vote(request):
    if request.method == 'POST':
        vote_type = request.POST['type']
        vid_id    = request.POST['id']

        # Using transactions and select_for_update we prevent data races
        with transaction.atomic():
            video = Video.objects.filter(pk=vid_id).select_for_update()[0]

            if vote_type == "up":
                video.points += 1
            if vote_type == "down":
                video.points -= 1

            video.save()



        return f"{vote_type}voted {video.title}!"
    else:
        raise Http404()
