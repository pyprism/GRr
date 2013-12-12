from django.db import models

# Create your models here.

class Users(models.Model):
	userName = models.CharField(max_length=30)
	userEmail = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

class File(models.Model):
	fileName = models.CharField(max_length=300)