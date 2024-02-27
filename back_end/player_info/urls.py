from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('players', views.PlayerViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('injuries', views.PlayerInjuriesAndBansAPIView.as_view())
]