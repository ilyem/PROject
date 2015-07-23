from django.db import models
class Card(models.Model):
	name = models.CharField(max_length=60)
	media_type=models.CharField(max_length=32)
	image= models.ImageField()
	url= models.URLField(max_length=200)


# Create your models here.
