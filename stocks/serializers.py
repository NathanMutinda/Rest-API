from rest_framework import serializers
from .models import Stocks


class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stocks
        fields = ("url", "id", "Amazon", "Facebook")

