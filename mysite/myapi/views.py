# views.py
from rest_framework import filters
from rest_framework import viewsets, generics

from .serializers import WishlistsSerializer
from .serializers import AvgBookRatingSerializer
from .serializers import BooksSerializer
from .serializers import GenresSerializer
from .serializers import PurchasedbooksSerializer
from .serializers import BookratingsSerializer
from .serializers import AddressesSerializer
from .serializers import AuthorsSerializer
from .serializers import UsersSerializer
from .serializers import CreditcardsSerializer
from .serializers import ShoppingcartsSerializer

from .models import Wishlists
from .models import Books
from .models import Genres
from .models import Bookratings
from .models import Purchasedbooks
from .models import Authors
from .models import Addresses
from .models import Users
from .models import Creditcards
from .models import Shoppingcarts

from django.db import IntegrityError  
from rest_framework.exceptions import APIException  
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from myapi.pagination import BookListPagination
from django.db.models.signals import post_delete
from django.dispatch import receiver


class WishlistsViewSet(viewsets.ModelViewSet): #ModelViewSet is a class that includes behind-the-scenes implementations for REST calls like GET, POST, and DELETE
    queryset = Wishlists.objects.all().order_by('id') #order the wishlist objects by id
    serializer_class = WishlistsSerializer #the serializer class that will be used for validating and deserializing input, and for serializing output
    
    @receiver(post_delete, sender=Wishlists) #calls the func if the user does a REST DELETE call
    def moveToShoppingCart(sender, instance, **kwargs): #function to remove the book from the wishlist and move it to the shopping cart
        bookid = Books.objects.get(id = instance.bookid.id) #get the bookid of the instance to be deleted
        userid = Users.objects.get(id = instance.userid.id) #get the userid of the instance to be deleted
        instanceShopping = Shoppingcarts(userid = userid, bookid = bookid) #create a Shoppingcart object with the userid and bookid of the deleted instance
        instanceShopping.save(force_insert=True) #save the new instance of Shoppingcart in the database
    
    def list(self, request):
        queryset = Wishlists.objects.all().order_by('id') #order the wishlist objects by id
        userid = self.request.query_params.get('userid') #get the userid inputted from the query parameters
        name = self.request.query_params.get('name') #get the name of the wishlist inputted from the query parameters
        
        if userid and not name: #if the userid has been inputted in the query params but the name has been left blank
            return Response("Please enter the name of the wishlist you wish to see.", status=status.HTTP_404_NOT_FOUND)
            
        if not userid and name: #if the name has been inputted in the query params but the userid has been left blank
            return Response("Please enter a userid.", status=status.HTTP_404_NOT_FOUND)
        
        if not Wishlists.objects.filter(userid = userid).exists() and userid: #if a userid has been inputted in the query params that doesn't exist
            return Response("The userid does not exist.", status=status.HTTP_404_NOT_FOUND)
        
        if not Wishlists.objects.filter(name = name).exists() and name: #if the name of the wishlist inputted in the query params does not belong to the user
            return Response("User " + userid + " does not have a wishlist with that name.", status=status.HTTP_404_NOT_FOUND)
        
        if userid and name: #if both the userid and name have been inputted successfully as query params without prior errors
            queryset = queryset.filter(userid=userid) #will return only the db rows containing the userid entered
            queryset = queryset.filter(name=name) #will return only the db rows containing the both the userid and name entered
            books = queryset.values('bookid', 'bookid__name') #will return only the db columns of the filtered queryset with the bookid and the name of the book
            return Response({"Books": list(books)})
        #The double underscores signify retrieving a value from another table by the foreign key
        queryset = queryset.values('id', 'userid', 'userid__firstname', 'bookid', 'bookid__name', 'name') #queryset that will be returned if query parameters have
                                                                                                          #not been inputted
        return Response({"Wishlist Results": list(queryset)})

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        #Integrity error due to Unique Constraint in models.py
        except IntegrityError as exc: #Error will be triggered if user inputs the same values for userid, bookid, and name twice.
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
    pagination_class = BookListPagination


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all().order_by('genre')
    serializer_class = GenresSerializer


class BookratingsViewSet(viewsets.ModelViewSet):
    queryset = Bookratings.objects.all().order_by('rating', 'ratingtimestamp', 'comment', 'commenttimestamp', 'bookid')
    serializer_class = BookratingsSerializer


class PurchasedbooksViewSet(viewsets.ModelViewSet):
    queryset = Purchasedbooks.objects.all().order_by('orderhistory', 'userid', 'bookid')
    serializer_class = PurchasedbooksSerializer

#viewset for users that will return all info of all users onto a single queryset.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Addresses.objects.all().order_by('id')
    serializer_class = AddressesSerializer

    def list(self, request):
        queryset = Addresses.objects.all().order_by('id')
        queryset = queryset.values('userid__username', 'userid__password', 'userid__firstname', 'userid__lastname',
                                   'userid__email', 'address', 'country', 'state', 'city', 'zipcode', )
        return Response({"User": list(queryset)})
    
#viewset that will search for a specific user using a URL based on either either username or email.
class UserSearchViewSet(generics.ListAPIView):
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer

    def list(self, request):
        queryset =  Addresses.objects.all()
        userinput = self.request.query_params.get('username')
        if userinput is not None and '@' in userinput:
            queryset = queryset.filter(userid__email=userinput)
            queryset = queryset.values('userid__username', 'userid__password', 'userid__firstname', 'userid__lastname', 'userid__email', 'address', 'country','state', 'city', 'zipcode',)
        elif userinput is not None and '@' not in userinput:
            queryset = queryset.filter(userid__username=userinput)
            queryset = queryset.values('userid__username', 'userid__password', 'userid__firstname', 'userid__lastname',
                                       'userid__email', 'address', 'country', 'state', 'city', 'zipcode', )
        return Response({"User": list(queryset)})

#viewset that will return all credit card info for all users on a single queryset. 
class CreditcardsViewSet(viewsets.ModelViewSet):
    queryset = Creditcards.objects.all().order_by('id')
    serializer_class = CreditcardsSerializer

#viewset that will search for a specific user's credit card info   
class creditcardSearchViewSet(generics.ListAPIView):
    queryset = Creditcards.objects.all()
    serializer_class = CreditcardsSerializer

    def list(self, request):
        queryset = Creditcards.objects.all()
        userinput = self.request.query_params.get('username')
        if userinput is not None and '@' in userinput:
            queryset = queryset.filter(userid__email=userinput)
            queryset = queryset.values('userid__username', 'userid__password', 'userid__firstname', 'userid__lastname',
                                   'userid__email', 'type', 'number', 'expirationdate', 'cvv')
        elif userinput is not None and '@' not in userinput:
            queryset = queryset.filter(userid__username=userinput)
            queryset = queryset.values('userid__username', 'userid__password', 'userid__firstname', 'userid__lastname',
                                       'userid__email', 'type', 'number', 'expirationdate', 'cvv')
        return Response({"User": list(queryset)})
 
    
class ShoppingcartsViewSet(viewsets.ModelViewSet):
    queryset = Shoppingcarts.objects.all().order_by('ordernumber')
    serializer_class = ShoppingcartsSerializer


class TopSellingBooksViewSet(generics.ListAPIView):
    queryset = Books.objects.all().order_by('-copiessold')[:10]
    serializer_class = BooksSerializer

    
class TopRatedBooksViewSet(generics.ListAPIView):
    queryset = Bookratings.objects.all().order_by('-rating')
    serializer_class = BookratingsSerializer


class AverageRatingViewSet(generics.ListAPIView):
    serializer_class = AvgBookRatingSerializer

    def get_queryset(self):
        return Books.objects.all()


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

class ISBNListsViewSet(generics.ListAPIView):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['isbn']

class RatingListsViewSet(generics.ListAPIView):
    serializer_class = BooksSerializer

    def get_queryset(self):
        queryset = Books.objects.all()

        try:
            user_input = self.request.query_params.get('rating')
        except AttributeError as abc:
            return Books.objects.none()

        if user_input is not None:

            try:
                queryset = queryset.filter(bookratings__rating__gte=user_input).all()

            except ValueError as abc:
                raise APIException("Rating should be a number")

            return queryset
        
        
class BookByAuthorListsViewSet(generics.ListAPIView):
    serializer_class = BooksSerializer
    def get_queryset(self):
        queryset = Books.objects.all()
        try:
            user_input = self.request.query_params.get('name').title().replace("-", " ")
            chunks = user_input.split()
        except AttributeError as abc:
            return Books.objects.none()
        if (user_input is not None and len(chunks) > 1):
            queryset = queryset.filter(authorid__firstname__icontains=chunks[0])
            queryset = queryset.filter(authorid__lastname__icontains=chunks[1])
        elif (user_input is not None):
            queryset = queryset.filter(authorid__firstname__icontains=user_input)
        return queryset
