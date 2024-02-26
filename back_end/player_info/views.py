from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from premier_league.models import TeamsChoices
from .models import Player, PlayerIjuriesAndBans, PlayerPositions
from .serializers import PlayerSerializer, PlayerInjuriesAndBansSerializer
# Create your views here.
class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(methods=['get'], detail=False)
    def dashboard(self, request):
        goals = self.get_queryset().order_by('-goals')[:10].values('first_name', 'last_name', 'team__name', 'goals')
        assists = self.get_queryset().order_by('-assists')[:10].values('first_name', 'last_name', 'team__name', 'assists')
        clean_sheets = self.get_queryset().filter(position=0).order_by('-clean_sheets')[:10].values('first_name', 'last_name', 'team__name', 'clean_sheets')

        return Response({'goals':goals, 'assists':assists, 'clean_sheets':clean_sheets}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def stats(self, request):
        stat = request.GET.get('stat', 'goals')
        club = request.GET.get('club')
        nation = request.GET.get('nation')
        position = request.GET.get('position')

        qs = Player.objects.all()

        if club and club != '-1':
            qs = qs.filter(team=club)
        if nation and nation != 'all nations':
            qs = qs.filter(nation=nation.upper())
        if position and position != '-1':
            qs = qs.filter(position=position)

        qs = qs.order_by(f'-{stat}').values('first_name', 'team', 'last_name', 'team__name', 'nation', stat)

        paginator = Paginator(qs, 10)
        page_num = request.GET.get('page', 1)

        page_obj = paginator.get_page(page_num).object_list

        filters = {'stat':['goals', 'assists', 'yellow_cards', 'red_cards', 'saves', 'clean_sheets'],
                   'nation':list(Player.objects.all().values_list('nation',flat=True).distinct()) + ['all nations'],
                   'team':TeamsChoices.choices + [(-1, 'all clubs')],
                   'position':PlayerPositions.choices + [(-1, 'all positions')]}
        return Response({'stat':page_obj, 'filters':filters}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def fantasy(self, request):
        qs = Player.objects.all().values('first_name', 'last_name', 'team__name', 'position', 'price', 'overall_points')
        return Response({'stats':qs}, status=status.HTTP_200_OK)

class PlayerInjuriesAndBansViewSet(ModelViewSet):
    queryset = PlayerIjuriesAndBans.objects.all()
    serializer_class = PlayerInjuriesAndBansSerializer
