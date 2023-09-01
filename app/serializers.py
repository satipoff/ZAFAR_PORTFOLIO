from rest_framework import serializers

from .models import Aloqa, AloqaTable



class AloqaTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = AloqaTable
        fields = ["icon", "tarmoq", "link_socialmedia"]




class AloqaSerializer(serializers.ModelSerializer):
    
    tables = AloqaTableSerializer(many=True)

    class Meta:
        model = Aloqa
        fields = ["title", "image", 'tables']


