# views.py
from rest_framework import viewsets, generics

from .serializers import WishlistsSerializer
from .serializers import BooksSerializer
from .serializers import GenresSerializer
from .serializers import PurchasedbooksSerializer
from .serializers import BookratingsSerializer
from .serializers import AddressesSerializer
from .serializers import AuthorsSerializer
from .serializers import UsersSerializer
from .serializers import CreditcardsSerializer

from .models import Wishlists
from .models import Books
from .models import Genres
from .models import Bookratings
from .models import Purchasedbooks
from .models import Authors
from .models import Addresses
from .models import Users
from .models import Creditcards

from django.db.models import Q
from django.db.models import Avg
from django.db import IntegrityError  # Import IntegrityError
from rest_framework.exceptions import APIException  # Import APIException
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response


class WishlistsViewSet(viewsets.ModelViewSet):
    queryset = Wishlists.objects.all().order_by('id')
    serializer_class = WishlistsSerializer

    def list(self, request):
        queryset = Wishlists.objects.all().order_by('id')
        userid = self.request.query_params.get('userid')
        name = self.request.query_params.get('name')
        if userid and name:
            queryset = queryset.filter(userid=userid)
            queryset = queryset.filter(name=name)
            books = queryset.values('bookid', 'bookid__name')
            return Response({"Books": list(books)})
        queryset = queryset.values('id', 'userid', 'userid__firstname', 'bookid', 'bookid__name', 'name')
        return Response({"Wishlist Results": list(queryset)})

    def delete(self, request, pk):
        instance = Wishlists.objects.get(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as exc:
            # return render("template.html", {"message": e.message})
            raise APIException("Cannot insert a book twice into the same wishlist")


class AddressesViewSet(viewsets.ModelViewSet):
    queryset = Addresses.objects.all().order_by('id')
    serializer_class = AddressesSerializer


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all().order_by('id')
    serializer_class = AuthorsSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('name')
    serializer_class = BooksSerializer


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all().order_by('genre')
    serializer_class = GenresSerializer


class BookratingsViewSet(viewsets.ModelViewSet):
    queryset = Bookratings.objects.all().order_by('-rating', 'ratingtimestamp', 'comment', 'commenttimestamp')
    serializer_class = BookratingsSerializer


class PurchasedbooksViewSet(viewsets.ModelViewSet):
    queryset = Purchasedbooks.objects.all().order_by('orderhistory', 'userid', 'bookid')
    serializer_class = PurchasedbooksSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UsersSerializer


class CreditcardsViewSet(viewsets.ModelViewSet):
    queryset = Creditcards.objects.all().order_by('id')
    serializer_class = CreditcardsSerializer


class TopSellingBooksViewSet(generics.ListAPIView):
    queryset = Books.objects.all().order_by('-copiessold')[:10]
    serializer_class = BooksSerializer


class TopRatedBooksViewSet(generics.ListAPIView):
    queryset = Bookratings.objects.all().order_by('-rating')
    serializer_class = BookratingsSerializer


class AverageRatingViewSet(generics.ListAPIView):
    serializer_class = BookratingsSerializer

    def get_queryset(self):
        queryset = Bookratings.objects.all()


        try:
            user_input = self.request.query_params.get('rating')
        except AttributeError as abc:
            return Bookratings.objects.none()

        if user_input is not None:
            queryset = queryset.filter(bookid=user_input).aggregate(Books_average=Avg('rating'))

            return queryset


class GenreListsViewSet(generics.ListAPIView):
    serializer_class = BooksSerializer

    def get_queryset(self):
        queryset = Books.objects.all()

        try:
            user_input = self.request.query_params.get('genre').title().replace("-", " ")
        except AttributeError as abc:
            return Books.objects.none()

        if user_input is not None:
            queryset = queryset.filter(genreid__genre=user_input)

            return queryset
