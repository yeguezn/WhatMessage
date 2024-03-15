from rest_framework import serializers
from .models import History

class HistorySerializer(serializers.Serializer):
    contact__full_name = serializers.CharField(max_length=50)
    message__content = serializers.CharField(max_length=150)
    message__category__name = serializers.CharField(max_length=15)
    date_time = serializers.DateTimeField()