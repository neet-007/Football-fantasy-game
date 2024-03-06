from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from .models import UserModel

class UserModelSerializer(ModelSerializer):
    has_team = SerializerMethodField('get_has_team')
    made_first_team = SerializerMethodField('get_made_first_team')
    class Meta:
        model = UserModel
        fields = ['pk', 'is_verified', 'is_admin', 'has_team', 'made_first_team']

    def get_has_team(self, obj):
        if obj.team_set.all().count() <= 0:
            return False
        return True

    def get_made_first_team(self, obj):
        temp =  obj.team_set.all()
        if not temp:
            return False

        return temp[0].made_first_team