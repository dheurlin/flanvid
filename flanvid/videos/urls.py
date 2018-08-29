from django.urls import path

from . import views

app_name = 'videos'
urlpatterns = [
    path('', views.index, name='index'),
    path('vote/', views.vote, name='vote'),
    path('vidlist/', views.vidlist, name='vidlist'),
]
