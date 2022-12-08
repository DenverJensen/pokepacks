import csv
from django.shortcuts import render
import os

from re import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Pokemon, CSVFile

from django.template import loader

# Create your views here.


def home(request):
    context = {}
    return render(request, 'pokepacks/home.html', context)


# packs are made up of 5 cards. default: 3 common, 2 rare
# each pack will then have a 1/5 chance for epic and 1/10 chance for legendary. 
# If successful, will replace one of the 5 cards in the pack randomly
def openPacks(request):
    print(request.method)
    if (request.method == 'POST'):
        commonMons = Pokemon.objects.all()
        print(commonMons)


        return render(request, 'pokepacks/open.html', {'pokemon_pulls':commonMons})
    return render(request, 'pokepacks/open.html', {})


#load pokemon data from pokemon.csv
def loadPacks(request):
    #clear all pokemon first to clear old data
    Pokemon.objects.all().delete()

    #get pokemon csv file in this directory
    workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
    c = open(os.path.join(workpath, 'pokemon.csv'), 'r')
    reader = csv.reader(c)

    #iterate csv and insert into DB
    for row in reader:
        _, created = Pokemon.objects.get_or_create(
            name=row[1],
            type1=row[2],
            type2=row[3],
            rarity=row[6],
            generation=row[4]
            )
    return render(request, 'pokepacks/home.html', {})
