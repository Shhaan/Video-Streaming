from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_img = models.ImageField(upload_to='covers/')
    playback_url = models.URLField()
    user = models.IntegerField()
