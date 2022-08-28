from django.urls import path
from etudiants import views

urlpatterns = [
    path('', views.ListeEtudiant.as_view()),
    path('<int:id>', views.EtudiantDetails.as_view()), #passer un id de type int une forme de castage
    path('liste/<int:etudiant_id>', views.PresenceListe.as_view()), 
    path('presence',views.PresenceViewCreate.as_view()),

]