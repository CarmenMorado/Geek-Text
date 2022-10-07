# serializers.py
from rest_framework import serializers

from .models import Wishlists
from .models import Books
from .models import Genres

class WishlistsSerializer(serializers.ModelSerializer):
    #userid = serializers.CharField(source='userid.firstname')
    #bookid = serializers.CharField(source='bookid.name')

    class Meta:
        model = Wishlists
        fields = ('id', 'userid', 'bookid', 'name')

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'isbn', 'authorid', 'genreid', 'name', 'description', 'price', 'publisher', 'yearpublished', 'copiessold')
        
class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('id', 'genre')
