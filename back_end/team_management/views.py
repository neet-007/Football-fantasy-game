from .models import Team, GameWeekTeam
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import TeamSerializer, GameWeekTeamSerializer
# Create your views here.

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def create(self, request, *args, **kwargs):
        if self.get_queryset().filter().exists():
            return Response({'error':'user can have one team'}, status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class GameWeekTeamViewSet(ModelViewSet):
    queryset = GameWeekTeam.objects.all()
    serializer_class = GameWeekTeamSerializer
