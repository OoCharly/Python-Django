from django.db import models
from datetime import datetime


class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Create your models here.
