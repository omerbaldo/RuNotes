from __future__ import unicode_literals

from django.db import models
from solo.models import SingletonModel

# Create your models here.

class post(models.Model): 
	title = models.CharField(max_length=4000, null=True, blank=False )
	display_info = models.TextField(max_length=4000, null=True, blank=False )
	info = models.TextField(max_length=4000, null=True, blank=False )
	image = models.FileField(null=True, blank=False, upload_to="posts/")
	
	def __str__(self): #to string
		return self.title

	def __unicode__(self): 
		return self.title


class terms(SingletonModel): 
	info = models.TextField(max_length=100000, null=True, blank=False )
	
	def __str__(self): #to string
		return "terms"

	def __unicode__(self): 
		return "terms"
