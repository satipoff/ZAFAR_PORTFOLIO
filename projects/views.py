from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import ProjectCategories, Projects, ProjectTableImages
from .serializers import (
    ProjectCategoriesSerializer,
    ProjectTableImagesSerializer,
    ProjectsSerializer,
)



class ProjectCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ProjectCategories.objects.all()
    serializer_class = ProjectCategoriesSerializer



class ProjectTableImagesViewSet(viewsets.ModelViewSet):
    queryset = ProjectTableImages.objects.all()
    serializer_class = ProjectTableImagesSerializer



class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer



class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Projects.objects.filter(categories__id=category_id)
        return queryset
    
