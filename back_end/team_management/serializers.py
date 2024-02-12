from .models import Team, GameWeekTeam, GameWeekPlayer, PlayerTransfer
from user_auth.serializers import UserModelSerializer
from player_info.serializers import PlayerSerializer
from rest_framework.serializers import ModelSerializer, ValidationError, ListField, DictField, IntegerField


class TeamSerializer(ModelSerializer):
    user = UserModelSerializer()
    class Meta:
        model = Team
        fields = '__all__'
        extra_kwargs = {
                    'user': {'required':False, 'read_only':True},
                    'overall_points': {'required':False, 'read_only':True},
                    'overall_rank': {'required':False, 'read_only':True},
                    'free_transfers': {'required':False},
                    'game_week_transfers_made': {'required':False},
                    'bank': {'required':False, 'read_only':True},
                    'team_value': {'required':False, 'read_only':True},
                    'bench_boost': {'required':False},
                    'free_hit': {'required':False},
                    'triple_captin': {'required':False},
                    'wild_card': {'required':False}
                }

class GameWeekPlayerSerializer(ModelSerializer):
    class Meta:
        model = GameWeekPlayer
        fields = '__all__'
        extra_kwargs = {
            'points':{'required':False},
        }

class GameWeekTeamSerializer(ModelSerializer):
    team = TeamSerializer()
    team_pk = IntegerField(write_only=True)
    players_pks = ListField(child=IntegerField(), allow_empty=False, min_length=11, max_length=11, write_only=True)
    bench_order = DictField(child=IntegerField(), allow_empty=False, min_length=4, max_length=4, write_only=True)
    players = GameWeekPlayerSerializer(many=True)
    class Meta:
        model = GameWeekTeam
        fields = '__all__'
        extra_kwargs = {
            'team':{},
            'game_week':{'required':False},
            'points':{'required':False}
        }

    def create(self, validated_data):
        return self.Meta.model.objects.create(
            team_pk = validated_data['team_pk'],
            starters = validated_data['players_pks'],
            benched_players = validated_data['bench_order']
        )

class PlayerTransferSerializer(ModelSerializer):
    player_in = PlayerSerializer()
    player_in_pk = IntegerField()
    player_out = PlayerSerializer()
    player_out_pk = IntegerField()

    class Meta:
        model = PlayerTransfer
        fields = '__all__'
        extra_kwargs = {
            'game_week':{'required':False},
            'points_cost':{'required':False},
        }