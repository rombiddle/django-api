from rest_framework import serializers

from .models import Video,Song,Artist,Album

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        # fields = ('url', 'title', 'song')
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        #fields = ('title', 'album', 'artist', 'url')
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # fields = ('name')
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        #fields = ('name', 'count')
        fields = '__all__'