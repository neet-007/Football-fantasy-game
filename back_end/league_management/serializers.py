from .models import League, LeagueTeam, H2HLeagueTeam
from rest_framework.serializers import ModelSerializer, ValidationError, IntegerField, SerializerMethodField
 
class LeagueTeamSerializer(ModelSerializer):
    class Meta:
        model = LeagueTeam
        fields = '__all__'
        extra_kwargs = {
            'position':{'required':False, 'read_only':True},
            'game_week_points':{'required':False, 'read_only':True},
            'overall_points':{'required':False, 'read_only':True},
        }

class H2HLeagueTeamSerializer(ModelSerializer):
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
    teams_league = SerializerMethodField(method_name='get_teams_league', read_only=True)
    teams_h2h = SerializerMethodField(method_name='get_teams_h2h', read_only=True)

    league_pk = IntegerField(required=False, write_only=True)
    team_pk = IntegerField(required=False, write_only=True)

    class Meta:
        model = League
        fields = '__all__'
        extra_kwargs = {
            'name':{'required':False},
            'owner':{'required':False},
            'admin':{'required':False},
            'num_of_players':{'required':False, 'read_only':True},
            'is_h2h':{'required':False},
            'starting_game_week':{'required':False},
            'allow_post_create_entry':{'required':False}
        }

    def validate(self, attrs):
        if attrs.get('name') and self.context.get('owner'):

            attrs['owner'] = self.context.get('owner')
            return super().validate(attrs)

        if self.context.get('league_pk'):
            attrs['league_pk'] = self.context.get('league_pk')
            attrs['team_pk'] = self.context.get('team_pk')
            return super().validate(attrs)

        raise ValidationError('provided data is invalid')

    def create(self, validated_data):
        try:
            validated_data.pop('league_pk')
        except KeyError:
            pass
        try:
            validated_data.pop('team_pk')
        except KeyError:
            pass

        return super().create(validated_data)

    def update(self, instance, validated_data):
        try:
            validated_data.pop('league_pk')
        except KeyError:
            pass
        try:
            validated_data.pop('team_pk')
        except KeyError:
            pass

        return super().update(instance, validated_data)

    def join_league(self, validated_data):
        return self.Meta.model.objects.add_league_team(league_pk=validated_data['league_pk'], team=validated_data['team_pk'])

    def join_h2h_league(self, validated_data):
        return self.Meta.model.objects.add_h2h_league_team(h2h_league_pk=validated_data['league_pk'], team=validated_data['team_pk'])

    def get_teams_league(self, obj):
        if obj.is_h2h:
            return None

        teams = obj.leagueteam_set.all()
        if not teams:
            return None

        return LeagueTeamSerializer(teams, many=True).data

    def get_teams_h2h(self, obj):
        if not obj.is_h2h:
            return None

        teams = obj.h2hleagueteam_set.all()
        if not teams:
            return None

        return H2HLeagueTeamSerializer(teams, many=True).data