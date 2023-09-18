from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

from ckeditor.fields import RichTextField




class ProjectCategories(MPTTModel):

    title = models.CharField(max_length=232)
    slug = models.SlugField(null=False, unique=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Projects(MPTTModel):

    title = models.CharField(max_length=232)
    desc = RichTextField(blank=True, null=True)
    categories = TreeForeignKey(to=ProjectCategories, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self) -> str:
        return self.title

    @property
    def formatted_created_at(self):
        return self.created_at.strftime('%d.%m.%Y')


    class Meta:

        verbose_name = "Proekt"
        verbose_name_plural = "Proektlar"



# Talbels
class ProjectTableImages(models.Model):
    project = TreeForeignKey(to=Projects, on_delete=models.CASCADE, related_name="project_table_images", blank=True, null=True)
    images = models.ImageField(upload_to='projects')




