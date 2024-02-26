from .models import PremierLeagueTeamBase, PremierLeagueTeam, TeamFixtures
from rest_framework.serializers import ModelSerializer, ValidationError

class PremierLeagueTeamBaseSerializer(ModelSerializer):
    class Meta:
        model = PremierLeagueTeamBase
        fields = '__all__'

class PremierLeagueTeamSerializer(ModelSerializer):
    base_team = PremierLeagueTeamBaseSerializer(required=False, read_only=True)
    class Meta:
        model = PremierLeagueTeam
        exclude = ('points_per_match', 'expected_goals_for', 'expected_goals_against', 'expected_goals_differance', 'expected_goals_differance_per_ninety')
        extra_kwargs = {
                    'name': {'required':False, 'read_only':True},
                    'team_code': {'required':False, 'read_only':True},
                    'postition': {'required':False, 'read_only':True},
                    'matches_played': {'required':False, 'read_only':True},
                    'wins': {'required':False, 'read_only':True},
                    'losses': {'required':False, 'read_only':True},
                    'draws': {'required':False, 'read_only':True},
                    'goals_for': {'required':False, 'read_only':True},
                    'goals_against': {'required':False, 'read_only':True},
                    'goals_differance': {'required':False, 'read_only':True},
                    'points': {'required':False, 'read_only':True},
                    'points_per_match': {'required':False, 'read_only':True},
                    'expected_goals_for': {'required':False, 'read_only':True},
                    'expected_goals_against': {'required':False, 'read_only':True},
                    'expected_goals_differance': {'required':False, 'read_only':True},
                    'expected_goals_differance_per_ninety': {'required':False, 'read_only':True},
                    'last_five': {'required':False, 'read_only':True}
        }

class TeamFixturesSerializer(ModelSerializer):
    team = PremierLeagueTeamBaseSerializer()
    opponent = PremierLeagueTeamBaseSerializer()
    class Meta:
        model = TeamFixtures
        fields = '__all__'
        extra_kwargs = {
            'team': {'required':False, 'read_only':True},
            'date': {'required':False, 'read_only':True},
            'comp': {'required':False, 'read_only':True},
            'game_week': {'required':False, 'read_only':True},
            'day': {'required':False, 'read_only':True},
            'ground': {'required':False, 'read_only':True},
            'result': {'required':False, 'read_only':True},
            'goals_for': {'required':False, 'read_only':True},
            'goals_against': {'required':False, 'read_only':True},
            'opponent': {'required':False, 'read_only':True}
        }