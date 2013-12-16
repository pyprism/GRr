from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class File(models.Model):
	user = models.ForeignKey(User)
	fileList = models.CharField(max_length=400 , verbose_name = "Files")
	filePermission = models.CharField(max_length=30, verbose_name = "File Permission")

	def __unicode__(self):
		return u'%s %s %s' % (self.user, self.fileList, self.counter)