from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import UsersSerializer
from .serializers import CreditcardsSerializer
from .models import Users
from .models import Creditcards


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UsersSerializer


class CreditcardsViewSet(viewsets.ModelViewSet):
    queryset = Creditcards.objects.all().order_by('id')
    serializer_class = CreditcardsSerializer
