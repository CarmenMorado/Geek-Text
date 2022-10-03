# serializers.py
from rest_framework import serializers

from .models import Wishlists
from .models import Addresses
from .models import Authors

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('id', 'firstname', 'lastname', 'biography', 'publisher')

class WishlistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlists
        fields = ('UserID', 'BookID', 'name')
             
class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ('id', 'userid', 'type', 'address', 'country', 'state', 'city', 'zipcode')

