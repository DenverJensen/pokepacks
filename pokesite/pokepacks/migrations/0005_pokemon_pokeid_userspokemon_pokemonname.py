# Generated by Django 4.1.3 on 2022-12-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokepacks', '0004_alter_userspokemon_daterolled'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='pokeID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userspokemon',
            name='pokemonName',
            field=models.CharField(default='', max_length=200),
        ),
    ]