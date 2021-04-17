from rest_framework import serializers
from log.models import Log
from datetime import datetime

class LogSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField('getdate')

    def getdate(self, obj):
        return datetime.strftime(obj.log_date, "%d/%m/%Y %H:%M")
    class Meta:
        model = Log
        exclude = ['log_date', ]