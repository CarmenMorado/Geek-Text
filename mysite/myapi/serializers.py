# serializers.py
from rest_framework import serializers

from .models import Wishlists
from .models import Books
from .models import Genres

class WishlistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlists
        fields = ('userid', 'bookid', 'name')
             
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('isbn', 'authorid', 'genreid', 'name', 'description', 'price', 'publisher', 'yearpublished', 'copiessold')
        
class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('id', 'genre')


