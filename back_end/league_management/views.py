from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.contrib.auth.models import AnonymousUser
from team_management.models import Team
from .models import League, LeagueTeam, H2HLeagueTeam
from .serializers import LeagueSerializer, LeagueTeamSerializer
# Create your views here.

class LeagueViewSet(ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

    @action(detail=False, methods=['get'])
    def user_leagues(self, request):
        if request.user == AnonymousUser:
            return Response({'error':'user is not logged in'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            team = Team.objects.get(user=request.user)
        except Team.DoesNotExist:
            return Response({'error':'player must have a team'}, status=status.HTTP_400_BAD_REQUEST)

        leagues_classic = LeagueTeam.objects.filter(team=team).values('league__name', 'position', 'last_position')
        leagues_h2h = H2HLeagueTeam.objects.filter(team=team).values('league__name', 'position', 'last_position')

        return Response({'classic_leagues':leagues_classic, 'h2h_leagues':leagues_h2h}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put'])
    def join_league(self, request, pk=None):
        context = {}
        context['league_pk'] = self.kwargs.get('pk')
        try:
            context['team_pk'] = Team.objects.filter(user=request.user).values_list('pk')[0][0]
        except Team.DoesNotExist:
            return Response('user is anonymous or doesnt have a team')

        serialized_data = LeagueSerializer(data={}, context=context)
        if serialized_data.is_valid():
            try:
                serialized_data.join_league(validated_data=serialized_data.validated_data)
            except ValueError as ve:
                return Response({'error':f'{str(ve)}'})

            return Response({'success':'joined league'}, status=status.HTTP_201_CREATED)

        return Response({'error':serialized_data.errors.values()}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def leave_league(self, request, pk=None):
        try:
            team = Team.objects.get(user=request.user)
        except Team.DoesNotExist:
            return Response({'error':'user must have a team'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            league_team = LeagueTeam.objects.get(league__pk=pk, team=team)
        except LeagueTeam.DoesNotExist:
            return Response({'error':'team is not in this league'}, status=status.HTTP_400_BAD_REQUEST)

        League.objects.remove_league_team(league_team=league_team, league_pk=pk)
        return Response({'success':'team removed from league'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put'])
    def join_h2h_league(self, request, pk=None):
        context = {}
        context['league_pk'] = self.kwargs.get('pk')
        try:
            context['team_pk'] = Team.objects.filter(user=request.user).values_list('pk')[0][0]
        except Team.DoesNotExist:
            return Response('user is anonymous or doesnt have a team')

        serialized_data = LeagueSerializer(data={}, context=context)
        if serialized_data.is_valid():
            try:
                serialized_data.join_h2h_league(validated_data=serialized_data.validated_data)
            except ValueError as ve:
                return Response({'error':f'{str(ve)}'})

            return Response({'success':'joined league'}, status=status.HTTP_201_CREATED)

        return Response({'error':serialized_data.errors.values()}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def leave_h2h_leauge(self, request, pk=None):
        try:
            team = Team.objects.get(user=request.user)
        except Team.DoesNotExist:
            return Response({'error':'user must have a team'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            league_team = H2HLeagueTeam.objects.get(league__pk=pk, team=team)
        except H2HLeagueTeam.DoesNotExist:
            return Response({'error':'team is not in this league'}, status=status.HTTP_400_BAD_REQUEST)

        League.objects.remove_h2h_league_team(h2h_league_team=league_team, h2h_league_pk=pk)
        return Response({'success':'team removed from league'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['delete'])
    def remove_team(self, request, pk=None):
        pass

    def get_serializer_context(self):
        context = super().get_serializer_context()

        try:
            context['owner'] = Team.objects.get(user=self.request.user)
        except Team.DoesNotExist:
            return Response('user is anonymous or doesnt have a team')

        return context