from django.db import models

class MyWatchList(models.Model):
    watched = models.TextField()
    title = models.CharField(max_length=50)
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.TextField()
