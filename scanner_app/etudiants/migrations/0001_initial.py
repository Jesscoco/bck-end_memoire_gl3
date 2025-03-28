# Generated by Django 3.2.12 on 2022-08-22 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenoms', models.CharField(max_length=100)),
                ('matricule', models.IntegerField(unique='TRUE')),
                ('telephone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=100)),
                ('specialite', models.CharField(max_length=100)),
                ('code_specialite', models.CharField(max_length=100)),
                ('annee_academique', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('etudiants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etudiants.etudiant', verbose_name='')),
            ],
        ),
    ]
