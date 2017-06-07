from django.db import models

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
	title = models.CharField(max_length=100)
	song = models.OneToOneField("Song", null=True, blank=True)
	def __str__(self):
		return '%s' % (self.title)
	def save(self, *args, **kwargs):
		# acces api youtube
		self.title = 
		super(Video, self).save(*args, **kwargs)

class Song(models.Model):
	title = models.CharField(max_length=100)
	album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
	artist = models.ManyToManyField(Artist)
	url = models.CharField(max_length=200, null=True, blank=True)
	def __str__(self):
		return '%s' % (self.title)
	def save(self, *args, **kwargs):
		Video.objects.get_or_create(url='http://www.google.fr', song=self)
		super(Song, self).save(*args, **kwargs)
