from django.db import models
from django.utils import timezone
import json
import requests

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return '%s' % (self.name)

class Album(models.Model):
	name = models.CharField(max_length=50)
	count = models.IntegerField(default=0)
	def __str__(self):
		return '%s' % (self.name)

class Video(models.Model):
	url = models.CharField(max_length=200, unique= True)
	title = models.CharField(max_length=100, null=True, blank=True)
	song = models.OneToOneField("Song", null=True, blank=True)
	def __str__(self):
		return '%s' % (self.title)
	def save(self, *args, **kwargs):
		# acces api youtube
		# clé api youtube : AIzaSyCCBAi0RJ12qEz1yag8O24BWrW9rhB1gpw
		url2 = self.url
		res = url2.rsplit('=', 1)[1]
		urlfinal = 'https://www.googleapis.com/youtube/v3/videos?id='+res+'&key=AIzaSyCCBAi0RJ12qEz1yag8O24BWrW9rhB1gpw&part=snippet'
		print(urlfinal)
		r = requests.get(urlfinal)
		data = json.loads(r.text)
		for i in data['items']:
			self.title = i['snippet']['title']
		super(Video, self).save(*args, **kwargs)

class Song(models.Model):
	title = models.CharField(max_length=100)
	album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
	artist = models.ManyToManyField(Artist)
	url = models.CharField(max_length=200, null=True, blank=True)
	def __str__(self):
		return '%s' % (self.title)
	def save(self, *args, **kwargs):
		super(Song, self).save(*args, **kwargs)
		print(self)
		video, created = Video.objects.get_or_create(url=self.url, defaults={'song': self})
		if not created:
			old_song = Song.objects.get(pk=video.song.pk)
			old_song.url = ""
			old_song.save()
			print(old_song)
			video.song = self
			video.save()

class Token(models.Model):
	user = models.OneToOneField('auth.User', on_delete=models.CASCADE, unique=True)
	hash = models.CharField(max_length=100)
	# expiration_date = models.DateTimeField(default=get_expiration_date)
	expiration_date = models.DateTimeField(timezone.now())

	def is_expired(self):
		return self.expiration_date < timezone.now()