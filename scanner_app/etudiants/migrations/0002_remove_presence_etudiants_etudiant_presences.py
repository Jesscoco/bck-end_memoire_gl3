# Generated by Django 4.1.1 on 2022-10-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presence',
            name='etudiants',
        ),
        migrations.AddField(
            model_name='etudiant',
            name='presences',
            field=models.ManyToManyField(to='etudiants.presence'),
        ),
    ]
