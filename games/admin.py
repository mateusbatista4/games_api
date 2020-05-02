from django.contrib import admin
from .models import Game, Player, PlayerScore, EsrbRating

# Register your models here.

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(PlayerScore)
admin.site.register(EsrbRating)