from django.contrib import admin
from .models import Etudiant, Presence

# Register your models here.

admin.site.register(Etudiant)
admin.site.register(Presence)
