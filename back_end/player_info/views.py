from django.core.paginator import Paginator, EmptyPage
from django.core.exceptions import FieldError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from premier_league.models import TeamsChoices
from .models import Player, PlayerIjuriesAndBans, PlayerPositions, PlayerIjuriesAndBansStatusChoices
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
        sort = request.GET.get('sort', 'decs')
        stat = request.GET.get('stat', 'goals')
        club = request.GET.get('club')
        nation = request.GET.get('nation')
        position = request.GET.get('position')

        qs = Player.objects.exclude(goals=None, assists=None, nation=None, team=None)

        if club and club != '-1':
            qs = qs.filter(team=club)
        if nation and nation != 'all nations':
            qs = qs.filter(nation=nation.upper())
        if position and position != '-1':
            qs = qs.filter(position=position)

        if sort.lower() == 'decs':
            qs = qs.order_by(f'-{stat}').values('first_name', 'team', 'last_name', 'team__name', 'nation', stat)
        elif sort.lower() == 'acs':
            qs = qs.order_by(f'{stat}').values('first_name', 'team', 'last_name', 'team__name', 'nation', stat)
        else:
            return Response({'error':'sort must be acs or decs'}, status=status.HTTP_400_BAD_REQUEST)

        paginator = Paginator(qs, 10)
        page_num = request.GET.get('page', 1)

        page_dict = {}
        page_obj = paginator.get_page(page_num)

        try:
            page_dict['next'] = page_obj.next_page_number()
        except EmptyPage:
            page_dict['next'] = -1

        try:
            page_dict['prev'] = page_obj.previous_page_number()
        except EmptyPage:
            page_dict['prev'] = -1

        page_dict['num_of_pages'] = paginator.num_pages

        filters = {'stat':[['goals', 'assists', 'yellow_cards', 'red_cards', 'saves', 'clean_sheets'], request.GET.get('selected_stat', 'goals')],
                   'nation':[list(Player.objects.all().values_list('nation',flat=True).distinct()) + ['all nations'], request.GET.get('selected_nation', 'all nations')],
                   'team':[TeamsChoices.choices + [(-1, 'all clubs')], request.GET.get('selected_club', -1)],
                   'position':[PlayerPositions.choices + [(-1, 'all positions')], request.GET.get('selected_position', -1)]}
        return Response({'stat':page_obj.object_list, 'filters':filters, 'page':page_dict}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def fantasy_stats(self, request):
        sort = request.GET.get('sort', 'price')
        club = request.GET.get('club')
        position = request.GET.get('position')

        qs = Player.objects.all().values('first_name', 'last_name', 'team__name', 'position', 'price', 'overall_points')
        if club and club != '-1':
            qs = qs.filter(team=club)

        if position and position != '-1':
            qs = qs.filter(position=position)

        try:
            qs = qs.order_by(f'-{sort}')
        except FieldError:
            return Response({'error':f'field:{sort} is not valid'}, status=status.HTTP_400_BAD_REQUEST)

        paginator = Paginator(qs, 10)
        page_num = request.GET.get('page', 1)

        page_dict = {}
        page_obj = paginator.get_page(page_num)

        try:
            page_dict['next'] = page_obj.next_page_number()
        except EmptyPage:
            page_dict['next'] = -1

        try:
            page_dict['prev'] = page_obj.previous_page_number()
        except EmptyPage:
            page_dict['prev'] = -1

        page_dict['num_of_pages'] = paginator.num_pages

        fields = []
        for field in Player._meta.get_fields():
            if field.name in ['first_name', 'last_name', 'nation', 'position', 'age', 'team' ,"gameweekplayer", "player_transfer_player_in","player_transfer_player_out","playerijuriesandbans","id",]:
                continue
            fields.append(field.name)

        filters = {
            'sort':[fields, sort],
            'team':[TeamsChoices.choices + [(-1, 'all clubs')], request.GET.get('selected_club', -1)],
            'position':[PlayerPositions.choices + [(-1, 'all positions')], request.GET.get('selected_position', -1)]
        }
        return Response({'stat':page_obj.object_list, 'filters':filters, 'page':page_dict}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def fantasy_players(self, request):
        sort = request.GET.get('sort', 'price')
        club = request.GET.get('club')
        position = request.GET.get('position')

        qs = Player.objects.all().values('id', 'first_name', 'last_name', 'team__name', 'position', 'price', 'overall_points')
        if club and club != '-1':
            qs = qs.filter(team=club)

        if position and position != '-1':
            qs = qs.filter(position=position)

        try:
            qs = qs.order_by(f'-{sort}')
        except FieldError:
            return Response({'error':f'field:{sort} is not valid'}, status=status.HTTP_400_BAD_REQUEST)

        paginator = Paginator(qs, 20)
        page_num = request.GET.get('page', 1)

        page_dict = {}
        page_obj = paginator.get_page(page_num)

        players_dict = {}
        for player in page_obj.object_list:
            if not PlayerPositions(player['position']).label in players_dict:
                players_dict[PlayerPositions(player['position']).label] = [player]
            else:
                players_dict[PlayerPositions(player['position']).label].append(player)

        try:
            page_dict['next'] = page_obj.next_page_number()
        except EmptyPage:
            page_dict['next'] = -1

        try:
            page_dict['prev'] = page_obj.previous_page_number()
        except EmptyPage:
            page_dict['prev'] = -1

        page_dict['num_of_pages'] = paginator.num_pages
        page_dict['count'] = paginator.count

        fields = []
        for field in Player._meta.get_fields():
            if field.name in ['first_name', 'last_name', 'nation', 'position', 'age', 'team' ,"gameweekplayer", "player_transfer_player_in","player_transfer_player_out","playerijuriesandbans","id",]:
                continue
            fields.append(field.name)

        filters = {
            'sort':[fields, sort],
            'team':[TeamsChoices.choices + [(-1, 'all clubs')], request.GET.get('selected_club', -1)],
            'position':[PlayerPositions.choices + [(-1, 'all positions')], request.GET.get('selected_position', -1)]
        }
        return Response({'players':players_dict, 'filters':filters, 'page':page_dict}, status=status.HTTP_200_OK)

class PlayerInjuriesAndBansAPIView(APIView):
    def get(self, request, format=None):
        qs = PlayerIjuriesAndBans.objects.all()

        status = request.GET.get('status')
        club = request.GET.get('club')
        position = request.GET.get('position')

        if status and status != '-1':
            qs = qs.filter(status=status)
        if club and club != '-1':
            qs = qs.filter(team=club)
        if position and position != '-1':
            qs = qs.filter(player__position=position)
        try:
            qs = qs.order_by(f'-{request.GET.get('sort', 'status')}')
        except FieldError:
            return Response({'error':f'field:{request.GET.get('sort', 'price')} is not valid'}, status=status.HTTP_400_BAD_REQUEST)

        serilaized_qs = PlayerInjuriesAndBansSerializer(qs, many=True).data
        paginator = Paginator(serilaized_qs, 10)
        page_num = request.GET.get('page', 1)

        page_dict = {}
        page_obj = paginator.get_page(page_num)

        try:
            page_dict['next'] = page_obj.next_page_number()
        except EmptyPage:
            page_dict['next'] = -1

        try:
            page_dict['prev'] = page_obj.previous_page_number()
        except EmptyPage:
            page_dict['prev'] = -1

        page_dict['num_of_pages'] = paginator.num_pages

        filters = {
            'sort':[['status', 'return_date'], request.GET.get('sort', 'status')],
            'status':[PlayerIjuriesAndBansStatusChoices.choices, request.GET.get('selected_status', -1)],
            'team':[TeamsChoices.choices + [(-1, 'all clubs')], request.GET.get('selected_club', -1)],
            'position':[PlayerPositions.choices + [(-1, 'all positions')], request.GET.get('selected_position', -1)]
        }

        return Response({'stat':page_obj.object_list, 'filters':filters, 'page':page_dict})
