from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',  'goat_age', 'garden_array', 'hay_num', 'subscription_end_date', 'donated_goat_num')