# serializers.py
from rest_framework import serializers

from .models import Wishlists
from rest_framework import serializers

from .models import Users
from .models import Creditcards


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class CreditcardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creditcards
        fields = '__all__'
