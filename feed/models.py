from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.

class Post(models.Model):
    test = models.CharField(max_length=140, blank=False, null=False)
    image = ImageField()

    def __str__(self):
        return self.test

class Topic(models.Model):
    name = models.CharField(max_length=30, blank= False, null=False)
    description = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.name 