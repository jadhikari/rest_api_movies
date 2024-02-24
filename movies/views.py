from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviesdata
# Create your views here.



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviesdata.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviesdata.objects.filter(typ='action')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviesdata.objects.filter(typ__iexact='comedy')
    serializer_class = MovieSerializer