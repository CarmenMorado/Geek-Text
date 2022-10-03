# serializers.py
from rest_framework import serializers

from .models import Bookratings
from .models import Purchasedbooks


class BookratingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookratings
        fields = ('userID', 'bookID', 'rating','ratingtimestamp', 'comment', 'commenttimestamp')


class PurchasedbooksSerializer(serializers.ModelSerializer):
     class Meta:
        model = Purchasedbooks
        fields = ('orderhistory', 'userid', 'bookid')