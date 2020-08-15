from django.db import models

# Create your models here.
class List2018(models.Model):

    name = models.CharField(max_length=300)
    anime_id = models.IntegerField(default=10)
    summary = models.TextField(default="I am summary")
    no_of_episodes = models.IntegerField(default=100)
    dubbing= models.BooleanField(default=False)
    images = models.ImageField(upload_to ='animetitles')
    rating = models.IntegerField(default=10)
    link_crunchyroll= models.URLField(max_length=200)
    link_imdb= models.URLField(max_length=200)
    link_shop= models.URLField(max_length=200)
    up_votes = models.IntegerField(default=10)
    down_votes = models.IntegerField(default=10)



class Votes(models.Model):
  anime_id = models.IntegerField(default=0)
  user_id = models.IntegerField(default=0)