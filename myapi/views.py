# views.py
from rest_framework import viewsets
from .serializers import PurchasedbooksSerializer
from .serializers import BookratingsSerializer
from .models import Bookratings
from .models import Purchasedbooks

class BookratingsViewSet(viewsets.ModelViewSet):
    queryset = Bookratings.objects.all().order_by('rating', 'ratingtimestamp', 'comment', 'commenttimestamp')
    serializer_class = BookratingsSerializer

class PurchasedbooksViewSet(viewsets.ModelViewSet):
    queryset = Purchasedbooks.objects.all().order_by('orderhistory', 'userid', 'bookid')
    serializer_class= PurchasedbooksSerializer