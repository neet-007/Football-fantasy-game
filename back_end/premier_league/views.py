import datetime
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import PremierLeagueTeam, TeamFixtures, DayChoices
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
        qs = self.get_queryset().filter(goals_for=None, goals_against=None)

        team = request.GET.get('team', None)
        opponent = request.GET.get('opponent', None)
        time = request.GET.get('time', None)
        date = request.GET.get('date', None)

        if team:
            qs = qs.filter(team=team)
        if opponent:
            qs = qs.filter(opponent=opponent)
        if time:
            qs = qs.filter(time=time)
        if date:
            try:
                qs = qs.filter(date=datetime.datetime.strptime(date, "%Y-%m-%d").date())
            except:
                pass

        paginator = Paginator(qs, 10)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        return_dict = {}
        for record in page_obj:
            serilized_record = TeamFixturesSerializer(record).data
            if f'{record.date}-{record.get_day_display()}' in return_dict:
                return_dict[f'{record.date}-{record.get_day_display()}'].append(serilized_record)
                continue

            return_dict[f'{record.date}-{record.get_day_display()}'] = [serilized_record]

        return Response(return_dict, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def results(self, request):
        qs = self.get_queryset().exclude(goals_for=None, goals_against=None)

        team = request.GET.get('team', None)
        opponent = request.GET.get('opponent', None)
        time = request.GET.get('time', None)
        date = request.GET.get('date', None)

        if team:
            qs = qs.filter(team=team)
        if opponent:
            qs = qs.filter(opponent=opponent)
        if time:
            qs = qs.filter(time=time)
        if date:
            pass

        paginator = Paginator(qs, 10)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        return_dict = {}
        for record in page_obj:
            serilized_record = TeamFixturesSerializer(record).data
            if f'{record.date}-{record.get_day_display()}' in return_dict:
                return_dict[f'{record.date}-{record.get_day_display()}'].append(serilized_record)
                continue

            return_dict[f'{record.date}-{record.get_day_display()}'] = [serilized_record]

        return Response(return_dict, status=status.HTTP_200_OK)