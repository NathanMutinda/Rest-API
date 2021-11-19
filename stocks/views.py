from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import StockSerializer
from .models import Stocks


class StockView(viewsets.ModelViewSet):
    queryset = Stocks.objects.all()
    serializer_class = StockSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly),

