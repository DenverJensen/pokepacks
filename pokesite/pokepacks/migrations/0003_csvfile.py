# Generated by Django 4.1.3 on 2022-12-08 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokepacks', '0002_alter_pokemon_image_alter_pokemon_type2'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='csv_files/')),
            ],
        ),
    ]
