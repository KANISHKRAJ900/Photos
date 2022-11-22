from rest_framework import serializers
from .models import photo

class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = photo
        fields = ('id','img')

