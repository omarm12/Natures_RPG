from django.contrib import admin

# Register your models here.
from .models import Player, Observation

admin.site.register(Player)
admin.site.register(Observation)