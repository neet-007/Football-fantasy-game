from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from premier_league.serializers import PremierLeagueTeamBaseSerializer
from .models import Player, PlayerIjuriesAndBans

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class PlayerInjuriesAndBansSerializer(ModelSerializer):
    team = PremierLeagueTeamBaseSerializer()
    class Meta:
        model = PlayerIjuriesAndBans
        fields = '__all__'
