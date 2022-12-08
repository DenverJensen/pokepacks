from django.contrib import admin
from .models import Pokemon, UsersPokemon, CSVFile

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(UsersPokemon)
admin.site.register(CSVFile)

