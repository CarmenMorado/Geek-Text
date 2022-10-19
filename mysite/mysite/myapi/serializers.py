# serializers.py
from rest_framework import serializers
from .models import Bookratings
from .models import Purchasedbooks
from .models import Wishlists
from .models import Addresses
from .models import Authors
from .models import Books
from .models import Genres
from .models import Users
from .models import Creditcards


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('id', 'firstname', 'lastname', 'biography', 'publisher')

class WishlistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlists
        fields = ('id', 'userid', 'bookid', 'name')
             
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

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class CreditcardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creditcards
        fields = '__all__'