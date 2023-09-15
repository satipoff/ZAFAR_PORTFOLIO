from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import ProjectCategories, Projects, ProjectTableImages

class ProjectCategoriesAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('parent',)
    search_fields = ('title',)


admin.site.register(ProjectCategories, ProjectCategoriesAdmin)


class ProjectTableImagesInline(admin.TabularInline):
    model = ProjectTableImages
    extra = 1  


class ProjectsAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title', 'categories')
    list_display_links = ('indented_title',)
    list_filter = ('parent',)
    search_fields = ('title', 'desc')
    inlines = [ProjectTableImagesInline]  





admin.site.register(Projects, ProjectsAdmin)
