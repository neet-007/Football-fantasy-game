from .models import Team, GameWeekTeam
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import AnonymousUser
from .serializers import TeamSerializer, GameWeekTeamSerializer, PlayerTransferSerializer
# Create your views here.

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def create(self, request, *args, **kwargs):
        if self.get_queryset().filter(user=request.user).exists():
            return Response({'error':'user can have one team'}, status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user

        return context

class GameWeekTeamViewSet(ModelViewSet):
    queryset = GameWeekTeam.objects.all()
    serializer_class = GameWeekTeamSerializer

    @action(detail=False, methods=['get'])
    def user_team(self, request):
        if request.user == AnonymousUser:
            return Response({'error':'user is anonymous'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            team = Team.objects.get(user=request.user)
        except Team.DoesNotExist:
            return Response({'error':'user must have team'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer_class()
        return Response(serializer(self.get_queryset().filter(team=team)[0]).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def player_transfer(self, request):
        if request.user == AnonymousUser:
            return Response({'error':'user is anonymoues'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            team = Team.objects.get(user=request.user)
        except Team.DoesNotExist:
            return Response({'error':'user must have team'}, status=status.HTTP_400_BAD_REQUEST)

        serialized_data = PlayerTransferSerializer(data=request.data, context={'team':team})

        if serialized_data.is_valid():
            serialized_data.create(serialized_data.validated_data)
            return Response({'success':'player transfer made'}, status=status.HTTP_201_CREATED)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        team_pk = Team.objects.filter(user=self.request.user).values_list('pk', flat=True)

        if len(team_pk) != 1:
            return Response('user must have one team', status=status.HTTP_400_BAD_REQUEST)

        context['team_pk'] = team_pk[0]
        return context