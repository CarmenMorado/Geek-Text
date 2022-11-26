# views.py
from rest_framework import filters
from rest_framework import viewsets, generics

from .serializers import WishlistsSerializer
from .serializers import AvgBookRatingSerializer
from .serializers import BooksSerializer
from .serializers import GenresSerializer
from .serializers import PurchasedbooksSerializer
from .serializers import BookratingsSerializer
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
    
    #using Django's built-in signals to let user code get notified of certain actions
    @receiver(post_delete, sender=Wishlists) #calls the func if the user does a REST DELETE call
    def moveToShoppingCart(sender, instance, **kwargs): #function to remove the book from the wishlist and move it to the shopping cart
        bookid = Books.objects.get(id = instance.bookid.id) #get the bookid of the deleted instance
        userid = Users.objects.get(id = instance.userid.id) #get the userid of the deleted instance 
        instanceShopping = Shoppingcarts(userid = userid, bookid = bookid) #create a Shoppingcart object with the userid and bookid of the deleted instance
        instanceShopping.save(force_insert=True) #save the new Shoppingcart instance in the database
    
    def list(self, request): #func to handle query parameters or edit the response whenever a user does a regular REST GET call 
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
            queryset = queryset.filter(name=name) #will return only the db rows containing both the userid and name entered
            books = queryset.values('bookid', 'bookid__name') #will return only the db columns of the filtered queryset with the bookid and the name of the book
            return Response({"Books": list(books)})
        
        #The double underscores signify retrieving a value from another table by the foreign key
        queryset = queryset.values('id', 'userid', 'userid__firstname', 'bookid', 'bookid__name', 'name') #queryset that will be returned if query parameters have
                                                                                                          #not been inputted
        return Response({"Wishlist Results": list(queryset)})

    def create(self, request, *args, **kwargs): #func to catch a custom error
        try:
            return super().create(request, *args, **kwargs)
        #Integrity error due to Unique Constraint in models.py
        except IntegrityError as exc: #Error will be triggered if user inputs the same values for userid, bookid, and name twice.
            raise APIException("Cannot insert a book twice into the same wishlist")



class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all().order_by('id')
    serializer_class = AuthorsSerializer


# view that returns list of books
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('name') # selects all books and orders by name
    serializer_class = BooksSerializer # selects the serializer that is used
    pagination_class = BookListPagination # selects the pagination class that is used


# view that returns list of genres
class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all().order_by('genre') # selects all genres and orders by genre
    serializer_class = GenresSerializer # selects serializer that is used


class BookratingsViewSet(viewsets.ModelViewSet):
    queryset = Bookratings.objects.all().order_by('rating', 'ratingtimestamp', 'comment', 'commenttimestamp', 'bookid')
    serializer_class = BookratingsSerializer


class PurchasedbooksViewSet(viewsets.ModelViewSet):
    queryset = Purchasedbooks.objects.all().order_by('orderhistory', 'userid', 'bookid')
    serializer_class = PurchasedbooksSerializer

#viewset for users that will return all info of all users onto a single queryset.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UsersSerializer

    def list(self, request):
        queryset = Users.objects.all().order_by('id')
        queryset = queryset.values('id', 'username', 'password', 'firstname', 'lastname', 'email', 'address')
        return Response({"User": list(queryset)})
    
#viewset that will search for a specific user using a URL based on either either username or email.
class UserSearchViewSet(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def list(self, request):
        queryset = Users.objects.all()
        userinput = self.request.query_params.get('username')
        if userinput is not None and '@' in userinput:
            queryset = queryset.filter(email=userinput)
            queryset = queryset.values('id', 'username', 'password', 'firstname', 'lastname', 'email', 'address')
        elif userinput is not None and '@' not in userinput:
            queryset = queryset.filter(username=userinput)
            queryset = queryset.values('id', 'username', 'password', 'firstname', 'lastname', 'email', 'address')
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


# view that returns the top 10 best selling books
class TopSellingBooksViewSet(generics.ListAPIView):
    queryset = Books.objects.all().order_by('-copiessold')[:10] # selects all books and returns the the first 10 books ordered by copies sold in descending order
    serializer_class = BooksSerializer # selects the serializer that is used

    
class TopRatedBooksViewSet(generics.ListAPIView):
    queryset = Bookratings.objects.all().order_by('-rating')
    serializer_class = BookratingsSerializer


class AverageRatingViewSet(generics.ListAPIView):
    serializer_class = AvgBookRatingSerializer

    def get_queryset(self):
        return Books.objects.all()


# view wit genre query parameters
class GenreListsViewSet(generics.ListAPIView):
    serializer_class = BooksSerializer # selects the serializer that is used

    # methody to get queryset
    def get_queryset(self):
        queryset = Books.objects.all() # selects all book

        try:
            user_input = self.request.query_params.get('genre').title().replace("-", " ") # selects users input using from url 'genre='
        except AttributeError as abc:
            return Books.objects.none() # returns an empty set when an arrtibute error is thrown

        if user_input is not None:
            queryset = queryset.filter(genreid__genre=user_input) # selects books based on the genre that was entered by the user 

            return queryset # returns the queryset
        
class BookByAuthorListsViewSet(generics.ListAPIView):
    serializer_class = BooksSerializer # selects the serializer that is used
    def get_queryset(self): # methody to get queryset
        queryset = Books.objects.all() # selects all book
        try:
            user_input = self.request.query_params.get('name').title().replace("-", " ") # takes users input
            chunks = user_input.split() # Allows to separate first name from last name (if the user imput have two words separated by a blank space)
        except AttributeError as abc:
            return Books.objects.none()  # returns an empty set when an arrtibute error is thrown
        if (user_input is not None and len(chunks) > 1): # Allows to search by first name and last name separated by a blank space
            queryset = queryset.filter(authorid__firstname__icontains=chunks[0])
            queryset = queryset.filter(authorid__lastname__icontains=chunks[1])
        elif (user_input is not None): # Allows to search by only first name
            queryset = queryset.filter(authorid__firstname__icontains=user_input)
        return queryset # returns the queryset       

# This is used to search books by ISBN 
class ISBNListsViewSet(generics.ListAPIView):
    serializer_class = BooksSerializer # selects the serializer
    queryset = Books.objects.all()  # sets the queryset to all books
    filter_backends = [filters.SearchFilter]
    search_fields = ['isbn'] # selects the field that is searched

# view to return books based on a certain number and higher
class RatingListsViewSet(generics.ListAPIView): 
    serializer_class = BooksSerializer # selects the serializer

    def get_queryset(self, request):
        queryset = Books.objects.all() # sets the queryset to all books

        try:
            user_input = self.request.query_params.get('rating') # selects user input from url 'rating='
        except AttributeError as abc:
            return Books.objects.none() # returns an empty set when an attribut error is thrown

        if user_input is not None:

            try:
                queryset = queryset.filter(bookratings__rating__gte=user_input).all() # selects books based on the user input
                queryset = queryset.values('isbn', 'name', 'authorid__firstname', 'authorid__lastname', 'bookratings__rating') # selects the fields to return

            except ValueError as abc:
                raise APIException("Rating should be a number") # returns a message when a value error is thrown

            return Response({"Book": list(queryset)}) # returns the queryset
