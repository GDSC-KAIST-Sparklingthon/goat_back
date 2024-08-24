from rest_framework import serializers
from .models import User, Donation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',  'goat_age', 'grass_num', 'garden_array', 'subscription_end_date', 'donated_goat_num')