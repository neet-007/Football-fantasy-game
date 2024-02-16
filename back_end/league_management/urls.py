from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

routrer = DefaultRouter()
routrer.register('league', views.LeagueViewSet)

urlpatterns = [
    path('', include(routrer.urls))
]