from django.db import models
from django.utils import timezone


# Create your models here.


class Pokemon(models.Model):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=200)
    type1 = models.CharField(max_length=200)
    type2 = models.CharField(max_length=200, null="true", blank="true")
    image = models.CharField(max_length=500, default="none")
    rarity = models.CharField(max_length=500)
    generation = models.IntegerField()

class UsersPokemon(models.Model):

    pokemonID = models.IntegerField()
    UserID = models.IntegerField()
    dateRolled = models.DateField(default=timezone.now)

class CSVFile(models.Model):
    file = models.FileField(upload_to='csv_files/')