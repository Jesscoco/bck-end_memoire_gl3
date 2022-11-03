from dataclasses import field, fields
from rest_framework import serializers
from etudiants.models import Etudiant , Presence, Agenda, DateHeure

class EtudiantSerializers (serializers.ModelSerializer):
    #ajout du model(des champs)  que la classe Etudiant va utiliser
    class Meta: 
        model = Etudiant
        fields ='__all__'

class PresenceSerializers (serializers.ModelSerializer):

    #modifier la serialization du champ etudiants qui est dans le models presence
    #etudiants = EtudiantSerializers()
    #ajout du model(des champs)  que la classe Presence va utiliser
    class Meta:
        model = Presence
        fields = '__all__'

class DateHeureSerializers (serializers.ModelSerializer):

    #modifier la serialization du champ etudiants qui est dans le models presence
    #etudiants = EtudiantSerializers()
    #ajout du model(des champs)  que la classe Presence va utiliser
    class Meta:
        model = DateHeure
        fields = '__all__'

class AgendaSerializers (serializers.ModelSerializer):
    dates=DateHeureSerializers(many=True)
    #modifier la serialization du champ etudiants qui est dans le models presence
    #etudiants = EtudiantSerializers()
    #ajout du model(des champs)  que la classe Presence va utiliser
    class Meta:
        model = Agenda
        fields = '__all__'