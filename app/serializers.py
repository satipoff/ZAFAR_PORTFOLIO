from rest_framework import serializers
from .models import aloqa

class aloqaSerializer(serializers.ModelSerializer):
    class Meta:
        model = aloqa
        fields = '__all__'
