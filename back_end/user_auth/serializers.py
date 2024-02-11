from rest_framework.serializers import ModelSerializer, ValidationError
from .models import UserModel

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['pk', 'is_verified', 'is_admin']