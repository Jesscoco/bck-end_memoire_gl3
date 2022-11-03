from django.contrib import admin
from .models import Etudiant, Presence, Agenda, DateHeure

# Register your models here.

admin.site.register(Etudiant)
admin.site.register(Presence)
admin.site.register(Agenda)
admin.site.register(DateHeure)

