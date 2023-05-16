from django.contrib import admin
from .models import Playlist, Review, Song

# Register your models here.
admin.site.register(Playlist)
admin.site.register(Review)
admin.site.register(Song)
