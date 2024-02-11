from .models import Team, GameWeekTeam
from rest_framework.viewsets import ModelViewSet
from .serializers import TeamSerializer, GameWeekTeamSerializer
# Create your views here.

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class GameWeekTeamViewSet(ModelViewSet):
    queryset = GameWeekTeam.objects.all()
    serializer_class = GameWeekTeamSerializer