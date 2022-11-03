# Generated by Django 4.1.1 on 2022-10-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiants', '0005_remove_etudiant_agenda_remove_presence_nom'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateHeure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_specialite', models.CharField(max_length=100)),
                ('dates', models.ManyToManyField(to='etudiants.dateheure')),
            ],
        ),
    ]
