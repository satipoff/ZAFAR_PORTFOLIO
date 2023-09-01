from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets



from .serializers import AloqaSerializer
from .models import Aloqa


class AloqaSerializerViewSet(viewsets.ModelViewSet):

    queryset = Aloqa.objects.all()
    serializer_class = AloqaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    


