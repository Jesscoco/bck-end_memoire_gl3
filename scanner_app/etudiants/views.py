from typing import final
from unicodedata import lookup
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from etudiants.serializers import  *
from rest_framework.parsers import JSONParser
#from rest_framework.response import Response
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import datetime
from django.db.models import Q
from bs4 import BeautifulSoup

#afficher la liste des etudiants et permet la creation d'un etudiant
class ListeEtudiant(generics.ListCreateAPIView):
    serializer_class = EtudiantSerializers #le serialiser a utiliser
    queryset = Etudiant.objects.all()   #la requete permet de recuperer les infos dans la bd et de faire respecter le format des donnees

# permet de visualiser les details dun etudiant(mettre a jour, supprimer)
class EtudiantDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EtudiantSerializers
    lookup_field = 'id' # recuperer les infos par id
    queryset = Etudiant.objects.all() #la requete permet de faire respecter le format des donnees 

#afficher la liste de presence d'un etudiants 
class PresenceListe(generics.ListCreateAPIView):

    serializer_class = PresenceSerializers
    queryset = Presence.objects.all()

    def get(self, request, *args, **kwargs):
        etudiant = Etudiant.objects.get(id=kwargs['etudiant_id'])
        presences = etudiant.presences
        presences_serializer = PresenceSerializers(presences, many=True)
        return Response(presences_serializer.data)
         
#vu de presence de tous les etudiants et ajout de presence d'un etudiant
class PresenceViewCreate(generics.ListCreateAPIView):

    serializer_class = PresenceSerializers
    queryset = Presence.objects.all()   

#
@csrf_exempt 
def get_qr_code(request,url):
    if request.method == 'POST' or request.method== 'GET':
        print(url)
        #data= JSONParser().parse(request) # recuprere les data de la request avec une image
        #recuperer les datas par l'url
        #code_url = data['url']
        code_url = url
        response = requests.get(code_url,verify=False)
        if response.status_code == 200:
            html_doc= response.text
            soup = BeautifulSoup(html_doc, 'html.parser') #tranformer le html_doc en objet beautiful soup
            tables = soup.find_all('table') # recuperer tous les <> tables
            row_soup = BeautifulSoup('{}'.format(tables[0]), 'html.parser') #1<> table
            table_rows = row_soup.find_all('tr') #rechercher les <>tr
            table_row_soup = BeautifulSoup('{}'.format(table_rows), 'html.parser')
            data_rows = table_row_soup.find_all('th')
            etudiant_info=[]
            for data in data_rows:
                data_soup = BeautifulSoup('{}'.format(data), 'html.parser')
                etudiant_info.append(data_soup.th.string)

            #recuperer les infos du 2nd <> table
            rows_soup = BeautifulSoup('{}'.format(tables[1]), 'html.parser') #2<> table
            tables_rows = rows_soup.find_all('tr')[1] #rechercher les <>tr
            tables_rows_soup = BeautifulSoup('{}'.format(tables_rows), 'html.parser')
            datas_rows = tables_rows_soup.find_all('td')
            for datas in datas_rows:
                datas_soup = BeautifulSoup('{}'.format(datas), 'html.parser')
                if datas_soup.td.string != None:
                    etudiant_info.append(datas_soup.td.string) 
            date_details = datetime.datetime.strptime(etudiant_info[5], '%d/%m/%Y').strftime('%Y-%m-%d')
           #checker si un numero matricule est dejq enregistrer dans la bd
            etudiant = Etudiant.objects.filter(matricule = etudiant_info[2])
            print(etudiant)
            if etudiant:
                
                presence=Presence.objects.create()
                etudiant[0].presences.add(presence)
                etudiant[0].save()
            else:
                new_etudiant = Etudiant.objects.create(
                nom=etudiant_info[0], prenoms=etudiant_info[1],matricule=etudiant_info[2],
                telephone= etudiant_info[4],email=etudiant_info[3],date_naissance=date_details,
                lieu_naissance=etudiant_info[6],specialite=etudiant_info[9],
                code_specialite=etudiant_info[8],annee_academique=etudiant_info[7]
                )
                presence=Presence.objects.create()
                new_etudiant.presences.add(presence)
                new_etudiant.save()

            
    return JsonResponse({"status":True}, safe=False)

@csrf_exempt   
def get_filtered_students(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        annee_scolaire =data['anneeScolaire']
        classe = data['classe'] 
        filiere =data['filiere']
        date = data['date']
        filtered_date = datetime.datetime.strptime(date, '%Y-%m-%d')if date!=''else None
        #fn de recherche
        #words=[annee_scolaire,classe,filiere]
        etudiants = Etudiant.objects.all()
        #results = etudiant.filter(
       # Q(nom__exact="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"))
        # iterate through keywords
        results = etudiants.filter(Q(annee_academique__contains=annee_scolaire))
        ndresults = results.filter(Q(code_specialite__icontains=classe))
        results = ndresults.filter(Q(specialite__icontains=filiere))
        final_result = etudiants.filter(
        Q(nom__exact="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"))
        if filtered_date:
            for result in results:
                etudiant= Etudiant.objects.get(id=result.id)
                presences = etudiant.presences.all()
                presences_serializer = PresenceSerializers(presences, many=True)
                for presence in presences:
                    print(filtered_date.date())
                    print(presence.date.date())
                    if filtered_date.date() == presence.date.date():
                        final_result|= results
        else:
            final_result=results

        print(final_result)
        etudiants_serializers = EtudiantSerializers(final_result, many=True)  
    return JsonResponse({"status":True, "data":etudiants_serializers.data}, safe=False)
