from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import aloqa
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import aloqaSerializer
from rest_framework.response import Response
from rest_framework import status



class AloqaSerializerAPI(APIView, PageNumberPagination):
    page_size = 3
    serializer_class = aloqaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request,*args,**kwargs):
        res = aloqa.objects.all()
        uzb = self.paginate_queryset(res, request, view=self)
        serializer = self.serializer_class(uzb, many=True)
        return Response(data=serializer.data)


    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
