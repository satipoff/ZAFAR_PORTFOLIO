from django.db import models

from ckeditor.fields import RichTextField

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey



class Aloqa(MPTTModel):

    title = models.CharField(max_length=222)
    image = models.ImageField(upload_to="aloqa/%Y/%m/%d")
    # default
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
    


""" TabularInline uchun modellar """


class AloqaTable(MPTTModel):

    aloqa = TreeForeignKey(to=Aloqa, on_delete=models.CASCADE, related_name='aloqatable', blank=True, null=True)
    icon = models.ImageField(upload_to="image/%Y/%m/%d")
    tarmoq = models.CharField(max_length=233, verbose_name="Tarmoq nomi")
    link_socialmedia = models.URLField(max_length=233, verbose_name="Tarmoq havolasi")


    # default
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

