# Generated by Django 4.1.3 on 2022-12-09 07:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pokepacks', '0003_csvfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userspokemon',
            name='dateRolled',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
