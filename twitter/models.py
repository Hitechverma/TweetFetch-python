from django.db import models
# Create your models here.

class Haircut(models.Model):
	tweet = models.CharField(max_length=140)

