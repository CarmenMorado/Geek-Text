# views.py
from rest_framework import viewsets

from .serializers import WishlistsSerializer
from .models import Wishlists


class WishlistsViewSet(viewsets.ModelViewSet):
    queryset = Wishlists.objects.all().order_by('name')
    serializer_class = WishlistsSerializer
