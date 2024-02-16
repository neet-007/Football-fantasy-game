from django.contrib import admin
from .models import League, LeagueTeam, H2HLeagueTeam
# Register your models here.
admin.site.register(League)
admin.site.register(LeagueTeam)
admin.site.register(H2HLeagueTeam)
