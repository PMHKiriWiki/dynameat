# Generated by Django 4.0.8 on 2024-03-06 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asteroids', '0001_initial'),
        ('sightings', '0002_rename_sigthing_sighting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='asteroid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asteroid_sightings', to='asteroids.asteroid'),
        ),
    ]
