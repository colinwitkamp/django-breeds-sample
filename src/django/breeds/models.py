from django.db import models

# Create your models here.

class Breed(models.Model):
    name = models.CharField(max_length=200)
    image_count = models.IntegerField(default=0)
    create_date = models.DateTimeField('date published')

class Style(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Image(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    path = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default=None)
