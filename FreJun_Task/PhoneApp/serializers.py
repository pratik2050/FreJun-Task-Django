from rest_framework import serializers
from PhoneApp.models import CallList

class CallListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallList
        fields = ('id', 'from_number', 'to_number', 'start_time')