from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Player, PlayerIjuriesAndBans

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class PlayerInjuriesAndBansSerializer(ModelSerializer):
    class Meta:
        model = PlayerIjuriesAndBans
        fields = '__all__'