from django.db import models

# Create your models here.

class Users(models.Model):
	userName = models.CharField(max_length=30)
	userEmail = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

class File(models.Model):
	user = models.ForeignKey(Users)
	fileName = models.CharField(max_length=400)
	counter = models.IntegerField()