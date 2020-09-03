from django.db import models

# Create your models here.
class RecommendationDatabase(models.Model):
    name = models.CharField(max_length=200)
    imdb = models.FloatField(default=0)
    image = models.ImageField(upload_to ='animetitles')
    summary = models.TextField()
    Year2010 = models.BooleanField(default=False)
    genre = models.CharField(max_length=15)
    sub_genre = models.CharField(max_length=15)
    crunchyroll = models.URLField(default="www.theanimeradio.com")
    info = models.URLField(default="www.theanimeradio.com")
