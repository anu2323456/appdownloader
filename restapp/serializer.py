from admininterface.models import *
from userinterface.models import *

from rest_framework import serializers

class AppcollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appcollections
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
