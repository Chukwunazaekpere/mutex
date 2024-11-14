from rest_framework import serializers
from .models import Logs

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        exclude = ["date_created"]