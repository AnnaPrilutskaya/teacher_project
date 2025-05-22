from django.contrib import admin
import os
from .models import Documents, Activities, Documents_for_measuring_materials, Measuring_materials, Lessons, Files_for_lesson
#from django_multiupload.admin import MultiUploadAdmin

#Уроки
class LessonFileInline(admin.TabularInline):
    model = Files_for_lesson
    extra = 1

@admin.register(Lessons)
class LessonAdmin(admin.ModelAdmin):
    inlines = [LessonFileInline]

@admin.register(Files_for_lesson)
class LessonFileAdmin(admin.ModelAdmin):
    list_display = ('get_original_filename', 'lesson')

#Измерительные материалы
class MeasuringMaterialsFileInline(admin.TabularInline):
    model = Documents_for_measuring_materials
    extra = 1

@admin.register(Measuring_materials)
class MeasuringMaterialsAdmin(admin.ModelAdmin):
    inlines = [MeasuringMaterialsFileInline]

@admin.register(Documents_for_measuring_materials)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('get_original_filename', 'measuring_material')

#Внеурочная деятельность
class ActivitiesFileInline(admin.TabularInline):
    model = Documents
    extra = 1

@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    inlines = [ActivitiesFileInline]

@admin.register(Documents)
class DocumentsActivityAdmin(admin.ModelAdmin):
    list_display = ('get_original_filename', 'activity')




