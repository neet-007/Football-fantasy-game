from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('teams', views.PremierLeagueTeamsViewSet)
router.register('fixtures', views.TeamFixturesViewSet)

urlpatterns = [
    path('', include(router.urls))
]