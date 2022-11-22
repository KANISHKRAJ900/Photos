from rest_framework import serializers
from .models import daily

class dailySerializer(serializers.ModelSerializer):
    class Meta:
        model = daily
        fields = ('id', 'title', 'sub_title', 'img','desc')