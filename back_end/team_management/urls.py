from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

routrer = DefaultRouter()
routrer.register('team', views.TeamViewSet)
routrer.register('game-week-team', views.GameWeekTeamViewSet)

urlpatterns = [
    path('', include(routrer.urls))
]