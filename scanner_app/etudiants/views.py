from unicodedata import lookup
from django.shortcuts import render
from rest_framework import generics 
from etudiants.serializers import  *

#afficher la liste des etudiants et permet la creation d'un etudiant
class ListeEtudiant(generics.ListCreateAPIView):
    serializer_class = EtudiantSerializers #le serialiser a utiliser
    queryset = Etudiant.objects.all()   #la requete permet de recuperer les infos dans la bd et de faire respecter le format des donnees

# permet de visualiser les details dun etudiant(mettre a jour, supprimer)
class EtudiantDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EtudiantSerializers
    lookup_field = 'id' # recuperer les infos par id
    queryset = Etudiant.objects.all() #la requete permet de faire respecter le format des donnees 

#afficher la liste de presence etudiants 
class PresenceListe(generics.ListCreateAPIView):
    serializer_class = PresenceSerializers
    #lookup_field = 'id'   
    queryset = Presence.objects.all()

