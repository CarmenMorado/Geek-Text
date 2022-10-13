# serializers.py
from rest_framework import serializers
from .models import Bookratings
from .models import Purchasedbooks
from .models import Wishlists
from .models import Addresses
from .models import Authors
from .models import Books
from .models import Genres

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('id', 'firstname', 'lastname', 'biography', 'publisher')

class WishlistsSerializer(serializers.ModelSerializer):
    #userid = serializers.CharField(source='userid.firstname')
    #bookid = serializers.CharField(source='bookid.name')
    class Meta:
        model = Wishlists
        fields = ('UserID', 'BookID', 'name')
             
class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ('id', 'userid', 'type', 'address', 'country', 'state', 'city', 'zipcode')

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'isbn', 'authorid', 'genreid', 'name', 'description', 'price', 'publisher', 'yearpublished', 'copiessold')
        
class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('id', 'genre')
        
class BookratingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookratings
        fields = ('userid', 'bookid', 'rating','ratingtimestamp', 'comment', 'commenttimestamp')

class PurchasedbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchasedbooks
        fields = ('orderhistory', 'userid', 'bookid')
