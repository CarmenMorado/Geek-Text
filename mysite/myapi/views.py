# views.py
from rest_framework import viewsets

from .serializers import WishlistsSerializer
from .serializers import BooksSerializer
from .serializers import GenresSerializer

from .models import Wishlists
from .models import Books
from .models import Genres

class WishlistsViewSet(viewsets.ModelViewSet):
    queryset = Wishlists.objects.all().order_by('name')
    serializer_class = WishlistsSerializer

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('name')
    serializer_class = BooksSerializer
    
class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all().order_by('genre')
    serializer_class = GenresSerializer
    
    