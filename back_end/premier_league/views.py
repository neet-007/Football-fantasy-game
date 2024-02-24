from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import PremierLeagueTeam, TeamFixtures
from .serializers import PremierLeagueTeamSerializer, TeamFixturesSerializer
# Create your views here.

class PremierLeagueTeamsViewSet(ModelViewSet):
    queryset = PremierLeagueTeam.objects.all()
    serializer_class = PremierLeagueTeamSerializer

class TeamFixturesViewSet(ModelViewSet):
    queryset = TeamFixtures.objects.all()
    serializer_class = TeamFixturesSerializer

    @action(methods=['get'], detail=False)
    def fixtures(self, request):
        qs = self.get_queryset().filter(goals_for=None, goals_against=None)[:20]
        return Response(TeamFixturesSerializer(qs, many=True).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def results(self, request):
        qs = self.get_queryset().exclude(goals_for=None, goals_against=None)[:20]
        return Response(TeamFixturesSerializer(qs, many=True).data, status=status.HTTP_200_OK)
