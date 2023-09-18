from rest_framework import serializers
from .models import ProjectCategories, Projects, ProjectTableImages



class ProjectCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategories
        fields = '__all__'



class ProjectTableImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTableImages
        fields = '__all__'



class ProjectsSerializer(serializers.ModelSerializer):
    project_table_images = ProjectTableImagesSerializer(many=True, read_only=True)
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = '__all__'

    def get_created_at(self, instance):
        return instance.created_at.strftime('%d.%m.%Y')

        