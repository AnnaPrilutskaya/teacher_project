from django.contrib import admin
import os
from .models import Recommendations, Files_for_Recommendation, TestNew, QuestionNew, AnswerOptionNew, Criterion
from nested_admin import NestedModelAdmin, NestedTabularInline
#from django_multiupload.admin import MultiUploadAdmin

#Советы и рекомендации
class RecommendationFileInline(admin.TabularInline):
    model = Files_for_Recommendation
    extra = 1

@admin.register(Recommendations)
class RecommendationAdmin(admin.ModelAdmin):
    inlines = [RecommendationFileInline]

@admin.register(Files_for_Recommendation)
class RecommendationFileAdmin(admin.ModelAdmin):
    list_display = ('get_original_filename', 'lesson')

#Тест
'''class AnswerInline(admin.TabularInline):  
    model = Answer
    extra = 3'''

'''@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline] 

admin.site.register(UserAnswer)'''

class AnswerOptionNewInline(NestedTabularInline):
    model = AnswerOptionNew
    extra = 3  # Количество пустых полей для ответов
    fields = ('text', 'points')

class QuestionNewInline(NestedTabularInline):
    model = QuestionNew
    extra = 1  # Количество пустых полей для вопросов
    show_change_link = True
    inlines = [AnswerOptionNewInline]

class CriterionInline(NestedTabularInline):
    model = Criterion
    extra = 1

@admin.register(TestNew)
class TestNewAdmin(NestedModelAdmin):
    inlines = [QuestionNewInline, CriterionInline]



'''@admin.register(QuestionNew)
class QuestionNewAdmin(admin.ModelAdmin):
    inlines = [AnswerOptionNewInline]'''