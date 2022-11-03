from datetime import date
import email
from email.policy import default
from tokenize import blank_re
from venv import create
from django.db import models

class Presence(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return '{}'.format(self.date)

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    matricule = models.IntegerField(unique='TRUE')
    telephone = models.CharField(max_length=100)
    email= models.EmailField( max_length=254)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    code_specialite = models.CharField(max_length=100)
    annee_academique = models.CharField(max_length=100)
    presences= models.ManyToManyField(Presence)
    
    def __str__(self) -> str:
        return '{} {}'.format(self.nom, self.prenoms)

class DateHeure(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self) -> str:
        return '{}'.format(self.nom)

class Agenda(models.Model):
    code_specialite = models.CharField(max_length=100)
    dates= models.ManyToManyField(DateHeure)

    def __str__(self) -> str:
        return '{}'.format(self.code_specialite)
