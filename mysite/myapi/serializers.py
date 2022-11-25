# serializers.py
from django.db.models import Avg
from rest_framework import serializers

from .models import Bookratings
from .models import Purchasedbooks
from .models import Wishlists
from .models import Authors
from .models import Books
from .models import Genres
from .models import Users
from .models import Creditcards
from .models import Shoppingcarts


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('id', 'firstname', 'lastname', 'biography', 'publisher')

class WishlistsSerializer(serializers.ModelSerializer):
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

class AvgBookRatingSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Bookratings
        fields = ("id", "average_rating")

    def get_average_rating(self, obj):
        # get the average rating for the book by the book id
        average_rating = Bookratings.objects.filter(bookid=obj.id).aggregate(
            Avg("rating")
        )["rating__avg"]
        # round the average rating to 2 decimal places
        if average_rating is not None:
            return round(average_rating, 2)
        else:
            return "0"        


class BookratingsSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Bookratings
        fields = (
            "userid",
            "bookid",
            "rating",
            "ratingtimestamp",
            "comment",
            "commenttimestamp",
            "avg_rating",
        )

    def get_avg_rating(self, obj):
        # Get the average rating for the book
        return Bookratings.objects.filter(bookid=obj.bookid).aggregate(Avg("rating"))

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
        
class ShoppingcartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoppingcarts
        fields = ('ordernumber', 'userid', 'bookid')
