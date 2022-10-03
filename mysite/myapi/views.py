# views.py
from rest_framework import viewsets

from .serializers import WishlistsSerializer
from .models import Wishlists

from .serializers import AddressesSerializer
from .models import Addresses

from .serializers import AuthorsSerializer
from .models import Authors

class WishlistsViewSet(viewsets.ModelViewSet):
    queryset = Wishlists.objects.all().order_by('name')
    serializer_class = WishlistsSerializer

class AddressesViewSet(viewsets.ModelViewSet):
    queryset = Addresses.objects.all().order_by('id')
    serializer_class = AddressesSerializer

class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all().order_by('id')
    serializer_class = AuthorsSerializer