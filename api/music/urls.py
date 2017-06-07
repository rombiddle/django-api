from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/artist', views.artist_list, name='artist-list'),
    url(r'^api/artist/(?P<pk>[0-9]+)/$', views.artist_detail, name='artist-detail'),
    url(r'^api/album', views.album_list, name='album-list'),
    url(r'^api/album/(?P<pk>[0-9]+)/$', views.album_detail, name='album-detail'),
    url(r'^api/song', views.song_list, name='song-list'),
    url(r'^api/song/(?P<pk>[0-9]+)/$', views.song_detail, name='song-detail'),
    url(r'^api/video', views.video_list, name='video-list'),
    url(r'^api/video/(?P<pk>[0-9]+)/$', views.video_detail, name='video-detail'),
]