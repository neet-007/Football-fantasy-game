from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

routrer = DefaultRouter()
routrer.register('team', views.TeamViewSet)

urlpatterns = [
    path('', include(routrer.urls))
]