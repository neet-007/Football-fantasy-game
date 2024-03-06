from .models import Team, GameWeekTeam, GameWeekPlayer, PlayerTransfer
from user_auth.serializers import UserModelSerializer
from player_info.serializers import PlayerSerializer
from .models import PlayerPositions
from rest_framework.serializers import ModelSerializer, ValidationError, ListField, DictField, IntegerField, FloatField, SerializerMethodField


class TeamSerializer(ModelSerializer):
    user = UserModelSerializer(required=False)
    favorite_team_pk = ListField(child=IntegerField() ,required=False, write_only=True)
    class Meta:
        model = Team
        fields = '__all__'
        extra_kwargs = {
                    'favorite_team': {'required':False, 'read_only':True},
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

    def validate(self, attrs):
        if attrs.get('name') and attrs.get('favorite_team_pk'):
            if len(attrs) != 2:
                raise ValidationError('can only pass name and favorite team when creating a team')

            if not self.context.get('user'):
                raise ValidationError('must provied a user')

            attrs['user'] = self.context['user']

            return super().validate(attrs)

        if (attrs.get('name') and not attrs.get('favorite_team_pk')) or (not attrs.get('name') and attrs.get('favorite_team_pk')):
            raise ValidationError('can only pass name and favorite team when creating a team')

        return super().validate(attrs)

class GameWeekPlayerSerializer(ModelSerializer):
    player = PlayerSerializer()
    class Meta:
        model = GameWeekPlayer
        fields = '__all__'
        extra_kwargs = {
            'points':{'required':False},
        }

class GameWeekTeamSerializer(ModelSerializer):
    team = TeamSerializer(read_only=True, required=False)
    team_pk = IntegerField(write_only=True, required=False)
    players_pks = ListField(child=ListField(child=IntegerField()), allow_empty=False, min_length=11, max_length=11, write_only=True)
    bench_order = DictField(child=ListField(child=IntegerField()), allow_empty=False, write_only=True)
    captins = DictField(child=IntegerField(), allow_empty=False, write_only=True)
    players = SerializerMethodField(method_name='get_players')
    transfers_dict = DictField(child=ListField(child=IntegerField()), required=False)

    class Meta:
        model = GameWeekTeam
        fields = '__all__'
        extra_kwargs = {
            'game_week':{'required':False},
            'points':{'required':False, 'read_only':True}
        }


    def create(self, validated_data):
        if 'transfers_dict' in validated_data:
            return self.Meta.model.objects.create_team_with_transfers(
                team_pk = self.context['team_pk'],
                starters = validated_data['players_pks'],
                bench_order = validated_data['bench_order'],
                captins = validated_data['captins'],
                transfers_dict = validated_data['transfers_dict']
            )

        return self.Meta.model.objects.create(
            team_pk = self.context['team_pk'],
            starters = validated_data['players_pks'],
            bench_order = validated_data['bench_order'],
            captins = validated_data['captins']
        )

    def get_players(self, obj):
        players = obj.game_week_player_game_week_team.all()
        player_dict = {
            'goalkeepers':{'starter':[], 'benched':[]},
            'defenders':{'starter':[], 'benched':[]},
            'midfielders':{'starter':[], 'benched':[]},
            'strikers':{'starter':[], 'benched':[]},
            'captins':{'captin':None, 'vice_captin':None}
        }
        for player in players:
            a = ''
            if player.position == 0:
                a = 'goalkeepers'
            if player.position == 1:
                a = 'defenders'
            if player.position == 3:
                a = 'midfielders'
            if player.position == 4:
                a = 'strikers'

            if player.captin == True:
                player_dict['captins']['captin'] = player.player.pk

            if player.vice_captin == False:
                player_dict['captins']['vice_captin'] = player.player.pk

            if player.starter:
                player_dict[a]['starter'].append({'id':player.player.id,'name':player.player.last_name, 'club':player.player.team.name, 'points':player.points, 'position':player.position, 'index':player.index, 'price':player.player.price, 'captin':player.captin, 'vice_captin':player.vice_captin, 'benched_order':player.benched_order})
            else:
                player_dict[a]['benched'].append({'id':player.player.id,'name':player.player.last_name, 'club':player.player.team.name, 'points':player.points, 'position':player.position, 'index':player.index, 'price':player.player.price, 'captin':player.captin, 'vice_captin':player.vice_captin, 'benched_order':player.benched_order})
        return player_dict

class PlayerTransferSerializer(ModelSerializer):
    player_in = PlayerSerializer(read_only=True, required=False)
    player_in_pk = IntegerField(write_only=True)
    player_out = PlayerSerializer(read_only=True, required=False)
    player_out_pk = IntegerField(write_only=True)

    def create(self, validated_data):
        validated_data['team'] = self.context.get('team')
        return self.Meta.model.objects.create(**validated_data)

    class Meta:
        model = PlayerTransfer
        fields = '__all__'
        extra_kwargs = {
            'team':{'required':False},
            'game_week':{'required':False},
            'points_cost':{'required':False},
        }