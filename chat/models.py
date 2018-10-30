from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class chatter(models.Model):
	# name = models.CharField(max_length=100)
	chat_field=models.TextField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)