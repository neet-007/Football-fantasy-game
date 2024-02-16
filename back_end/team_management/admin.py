from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(GameWeekPlayer)
admin.site.register(GameWeekTeam)
admin.site.register(PlayerTransfer)