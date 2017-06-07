from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ParseError
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Album,Artist,Song,Video
from .serializers import AlbumSerializer,ArtistSerializer,SongSerializer,VideoSerializer

@csrf_exempt
def artist_list(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            data = JSONParser.parse(request)
        except ParseError:
            return HttpResponse(status=400)
        serializer = ArtistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@csrf_exempt
def artist_detail(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        serializer = ArtistSerializer(artists, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artist.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
