from django.contrib import admin

# Register your models here.
from .models import Artist, Album, Song, Video

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Video)