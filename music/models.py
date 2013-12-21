from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Playlist(models.Model):
	user = models.ForeignKey(User)
	songName = models.CharField(max_length=128, verbose_name = "Song's Name")
	url = models.URLField(verbose_name = "Song's URL")
	favorite = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Playlist"

	def __unicode__(self):
		return self.songName