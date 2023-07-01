from django.db import models

# Create your models here.
class Film(models.Model):

    types = (
        ('film', 'film'),
        ('series', 'series'),
        ('anime film', 'anime_film'),
        ('anime series', 'anime_series')
    )

    name = models.CharField(max_length=64)
    language = models.CharField(max_length=2)
    rate = models.FloatField()
    type = models.CharField(max_length=64 ,choices=types)

    def __str__(self):
        return f"{self.id}: {self.name} , {self.language} , {self.rate}"