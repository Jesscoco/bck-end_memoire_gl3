from datetime import date
import email
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

