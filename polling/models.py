import datetime
from django.db import models
from django.utils import timezone


class Polls(models.Model):
    name_poll = models.CharField(max_length=200)
    poll_image = models.ImageField(upload_to ='polltitles')
    pub_date = models.DateTimeField('date published')
    poll_des = models.TextField()
    poll_id = models.IntegerField(default=0)


class Choices(models.Model):
    Polls = models.ForeignKey(Polls, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    choicedetail = models.TextField()
    image = models.ImageField(upload_to ='animetitles')
    votes = models.IntegerField(default=0)


class VotePolls(models.Model):
    user = models.IntegerField(default=0)
    poll = models.IntegerField(default=0)
