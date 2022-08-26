from dataclasses import field, fields
from rest_framework import serializers
from etudiants.models import Etudiant , Presence

class EtudiantSerializers (serializers.ModelSerializer):
    #ajout du model(des champs)  que la classe Etudiant va utiliser
    class Meta: 
        model = Etudiant
        fields ='__all__'

class PresenceSerializers (serializers.ModelSerializer):
    #ajout du model(des champs)  que la classe Presence va utiliser
    class Meta:
        model = Presence
        fields = '__all__'