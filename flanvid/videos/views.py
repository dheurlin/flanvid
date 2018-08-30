from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db import transaction

from django_ajax.decorators import ajax

import json

from .models import Video, VidVotes, VOTE_UP, VOTE_DOWN, vote_to_point
from .forms import VideoForm

def index(request):
    # Make sure the visitor's session is initiated
    if not 'voted_vids' in request.session:
        request.session['voted_vids'] = VidVotes().to_json()

    # Vaildate the submission form
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VideoForm()

    return render(request, 'videos/index.html', {
        'vid_form'  : form,
    })

def vidlist(request):
    vids_list = Video.objects.all().order_by('-points')
    return render(request, 'videos/vidlist.html', {
        'vids_list' : vids_list,
    })

@ajax
def vote(request):
    if request.method == 'POST':
        vote_type  = request.POST['type']
        vid_id     = request.POST['id']
        user_votes = VidVotes(json_data=request.session['voted_vids'])

        # Using transactions and select_for_update we prevent data races
        with transaction.atomic():
            video = Video.objects.filter(pk=vid_id).select_for_update()[0]

            # Adjust video vote according to whether the user has voted for the vid already

            if not user_votes.has_voted_for(vid_id):
                video.points += vote_to_point(vote_type)
                user_votes.add_vote(vid_id, vote_type)
            else:
                # Toggle vote if same vote is cast again:
                curr_vote = user_votes.get_vote_for(vid_id)
                if vote_type == curr_vote:
                    video.points -= vote_to_point(vote_type)
                    user_votes.remove_vote(vid_id)
                # otherwise, change the vote to the opposite
                else:
                    video.points += vote_to_point(vote_type) - vote_to_point(curr_vote)
                    user_votes.change_vote(vid_id, VOTE_UP if curr_vote == VOTE_DOWN else VOTE_DOWN)

            request.session['voted_vids'] = user_votes.to_json()
            video.save()

            return

    else:
        raise Http404()
