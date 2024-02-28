from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from .models import UserModel

class UserModelSerializer(ModelSerializer):
    has_team = SerializerMethodField('get_has_team')
    class Meta:
        model = UserModel
        fields = ['pk', 'is_verified', 'is_admin', 'has_team']

    def get_has_team(self, obj):
        if obj.team_set.all().count() <= 0:
            return False
        return True