import csv
from django.shortcuts import render
import os
import random

from re import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Pokemon, CSVFile, UsersPokemon
from django.core.paginator import Paginator


from django.template import loader

# Create your views here.
def home(request):
    context = {}
    return render(request, 'pokepacks/home.html', context)


# packs are made up of 5 cards. default: 3 common, 2 rare
# each pack will then have a 1/5 chance for epic and 1/10 chance for legendary.
# If successful, will replace one of the 5 cards in the pack randomly
def openPacks(request):
    message = ''
    if (request.method == 'POST'):
        
        #pull 3 commons
        commonMons = list(Pokemon.objects.filter(rarity="common"))
        comMons = random.sample(commonMons, 3)
        
        #pull 2 rare
        rare = list(Pokemon.objects.filter(rarity="rare"))
        rareMons = random.sample(rare, 2)
        pulledMons = comMons + rareMons 

        #roll for 1/5 chance at epic drop
        roll = random.randint(1, 5)
        if (roll == 5):
            epic = list(Pokemon.objects.filter(rarity="epic"))
            epicMons = random.sample(epic, 1)
            pulledMons.pop()
            pulledMons = pulledMons + epicMons 

        # roll 1/10 chance for legendary drop
        roll = random.randint(1, 10)
        if (roll == 10):
            legList = list(Pokemon.objects.filter(rarity="legendary"))
            legMons = random.sample(legList, 1)
            pulledMons.pop()
            pulledMons = pulledMons + legMons
        
        #insert pack into user collection
        for x in pulledMons:
            user_id = request.user.id # Get user_id from request
            UsersPokemon.objects.create(pokemonID=x.pokeID, UserID=user_id, pokemonName=x.name)

        return render(request, 'pokepacks/open.html', {
            'pokemon_pulls': pulledMons,
        })
    return render(request, 'pokepacks/open.html',{})


#load pokemon data from pokemon.csv
def loadPacks(request):
    #clear all pokemon first to clear old data
    Pokemon.objects.all().delete()

    #get pokemon csv file in this directory
    workpath = os.path.dirname(
        os.path.abspath(__file__))  #Returns the Path your .py file is in
    c = open(os.path.join(workpath, 'pokemon.csv'), 'r')
    reader = csv.reader(c)

    #iterate csv and insert into DB
    for row in reader:
        #only load first gen pokemon for now
        if(row[4]=='1'):
            _, created = Pokemon.objects.get_or_create(pokeID=row[0],
                                                    name=row[1],
                                                    type1=row[2],
                                                    type2=row[3],
                                                    rarity=row[6],
                                                    generation=row[4])
    return render(request, 'pokepacks/home.html', {})



def collection(request):
    message = 'collection'
    user_id = request.user.id # Get user_id from request

    usersIndexes = UsersPokemon.objects.filter(UserID=user_id)
    UsersPokemons = []
    for x in usersIndexes:
        # singlemonTest = list(Pokemon.objects.filter(pokeID=x.pokemonID))
        UsersPokemons.append(Pokemon.objects.filter(pokeID=x.pokemonID))
    listMons = list(UsersPokemons)
    print(listMons)
    # name = request.GET.get('pokemon_name')
    # if name != '' and name is not None:
    #     object = object.filter(name__icontains=name)

    return render(request, 'pokepacks/collection.html',{"messages":[message], "pokemon_pulls":UsersPokemons})


