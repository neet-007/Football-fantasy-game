from .models import Team, GameWeekTeam, GameWeekPlayer, PlayerTransfer
from user_auth.serializers import UserModelSerializer
from player_info.serializers import PlayerSerializer
from rest_framework.serializers import ModelSerializer, ValidationError, ListField, IntegerField


class TeamSerializer(ModelSerializer):
    user = UserModelSerializer()
    class Meta:
        model = Team
        fields = '__all__'
        extra_kwargs = {
                    'user': {'required':False, 'write_only':True},
                    'overall_points': {'required':False, 'write_only':True},
                    'overall_rank': {'required':False, 'write_only':True},
                    'free_transfers': {'required':False},
                    'game_week_transfers_made': {'required':False},
                    'bank': {'required':False, 'write_only':True},
                    'team_value': {'required':False, 'write_only':True},
                    'bench_boost': {'required':False},
                    'free_hit': {'required':False},
                    'triple_captin': {'required':False},
                    'wild_card': {'required':False}
                }

    def validate(self, attrs):

        return super().validate(attrs)

class GameWeekPlayerSerializer(ModelSerializer):
    class Meta:
        model = GameWeekPlayer
        fields = '__all__'
        extra_kwargs = {
            'points':{'required':False},
        }

class GameWeekTeamSerializer(ModelSerializer):
    team = TeamSerializer()
    players_pks = ListField(child=IntegerField(), allow_empty=False, min_length=11, max_length=11)
    players = GameWeekPlayerSerializer(many=True)
    class Meta:
        model = GameWeekTeam
        fields = '__all__'
        extra_kwargs = {
            'team':{},
            'game_week':{'required':False},
            'points':{'required':False}
        }

class PlayerTransferSerializer(ModelSerializer):
    player = PlayerSerializer()

    class Meta:
        model = PlayerTransfer
        fields = '__all__'
        extra_kwargs = {
            'game_week':{'required':False},
            'points_cost':{'required':False},
        }