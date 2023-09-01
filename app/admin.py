from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from .models import Aloqa, AloqaTable


""" Tables for Inline """

class AloqaTableInlines(admin.TabularInline):

   model = AloqaTable
   fields = ("icon", "tarmoq", "link_socialmedia")
   extra = 2


""" Models """

@admin.register(Aloqa)
class AloqaAdmina(DraggableMPTTAdmin):

   inlines = [AloqaTableInlines]

   fields = ("title", "image")




