from django.db import models
from django.urls import reverse
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('songs_detail', kwargs={'pk': self.id})

class Playlist(models.Model):
    title = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    songs = models.ManyToManyField(Song)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'playlist_id': self.id})

class Review(models.Model):
   date = models.DateField('Date of Play')
   rating = models.IntegerField(
    validators=[
            MinValueValidator(0),
            MaxValueValidator(7)
        ]
   )
   description = models.TextField(max_length=250)
   
   playlist = models.ForeignKey(
    Playlist,
    on_delete=models.CASCADE
    )
  
   class Meta:
    ordering = ['-date']

'''
class Photo(models.Model):
  url = models.CharField(max_length=200)
  playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for playlist_id: {self.playlist_id} @{self.url}"
'''