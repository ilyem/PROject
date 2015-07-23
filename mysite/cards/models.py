from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
class Card(models.Model):
	owner= models.ForeignKey(User)
	name = models.CharField(max_length=60)
	media_type=models.CharField(max_length=32)
	image= models.ImageField()
	url= models.URLField(max_length=200)
	created_at= models.DateTimeField()

	def __str__(self):
		return self.name


# Create your models here.
