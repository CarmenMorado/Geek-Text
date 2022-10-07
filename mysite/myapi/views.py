# views.py
from rest_framework import viewsets

from .serializers import WishlistsSerializer
from .serializers import BooksSerializer
from .serializers import GenresSerializer

from .models import Wishlists
from .models import Books
from .models import Genres


from django.db import IntegrityError # Import IntegrityError
from rest_framework.exceptions import APIException  #Import APIException
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
            
class WishlistsViewSet(viewsets.ModelViewSet):
    queryset = Wishlists.objects.all().order_by('id')
    serializer_class = WishlistsSerializer
    
    def delete(self, request, pk):
        instance = Wishlists.objects.get(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as exc:
            #return render("template.html", {"message": e.message})
            raise APIException("Cannot insert a book twice into the same wishlist")
            
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('name')
    serializer_class = BooksSerializer
    
class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all().order_by('genre')
    serializer_class = GenresSerializer
            
