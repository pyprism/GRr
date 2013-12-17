from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Playlist(models.Model):
	user = models.ForeignKey(User)
	url = models.URLField()
	songName = models.CharField(max_length=128, verbose_name = "Song Name")
	favorite = models.BooleanField(default=False)