from .models import League, LeagueTeam, H2HLeagueTeam
from rest_framework.serializers import ModelSerializer, ValidationError

class LeagueTeamSerializer(ModelSerializer):
    class Meta:
        model = LeagueTeam
        fields = '__all__'
        extra_kwargs = {
            'position':{'required':False, 'read_only':True},
            'game_week_points':{'required':False, 'read_only':True},
            'overall_points':{'required':False, 'read_only':True},
        }

class H2HLeagueTeam(ModelSerializer):
    class Meta:
        model = H2HLeagueTeam
        fields = '__all__'
        extra_kwargs = {
            'position':{'required':False, 'read_only':True},
            'games_played':{'required':False, 'read_only':True},
            'wins':{'required':False, 'read_only':True},
            'losses':{'required':False, 'read_only':True},
            'draws':{'required':False, 'read_only':True},
            'game_week_points':{'required':False, 'read_only':True},
            'score':{'required':False, 'read_only':True},
            'overall_points':{'required':False, 'read_only':True},
        }

class LeagueSerializer(ModelSerializer):
    teams_league = LeagueTeamSerializer(many=True, required=True)
    teams_h2h = H2HLeagueTeam(many=True, required=False)
    class Meta:
        model = League
        fields = '__all__'
        extra_kwargs = {
            'owner':{'required':False},
            'admin':{'required':False},
            'num_of_players':{'required':False, 'read_only':True},
            'is_h2h':{'required':False},
        }
