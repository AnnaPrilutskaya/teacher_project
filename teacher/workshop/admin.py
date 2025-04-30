from django.contrib import admin
import os
from .models import Documents, Activities, Documents_for_measuring_materials, Measuring_materials, Lessons, Files_for_lesson
#from django_multiupload.admin import MultiUploadAdmin


class LessonFileInline(admin.TabularInline):
    model = Files_for_lesson
    extra = 1

@admin.register(Lessons)
class LessonAdmin(admin.ModelAdmin):
    inlines = [LessonFileInline]

@admin.register(Files_for_lesson)
class LessonFileAdmin(admin.ModelAdmin):
    list_display = ('get_original_filename', 'lesson')


# Register your models here.
admin.site.register(Documents)
admin.site.register(Activities)
admin.site.register(Documents_for_measuring_materials)
admin.site.register(Measuring_materials)