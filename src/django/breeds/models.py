from django.db import models

# Create your models here.

class Breed(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField('date published')

class Style(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
