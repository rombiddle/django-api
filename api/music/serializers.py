from rest_framework import serializers

from .models import Video,Song,Artist,Album

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('url', 'title', 'song')

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'album', 'artist', 'url')

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name')

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('name', 'count')