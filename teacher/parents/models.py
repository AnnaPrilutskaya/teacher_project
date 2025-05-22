from django.db import models
import os
from ckeditor.fields import RichTextField


class Recommendations(models.Model):
    title = models.CharField('Название', max_length=200)
    content = RichTextField("Текст с форматированием", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Совет и рекомендация'
        verbose_name_plural = 'Советы и рекомендации'

class Files_for_Recommendation(models.Model):
    lesson = models.ForeignKey(Recommendations,
                               on_delete=models.CASCADE,
                               related_name='files',
                               blank=True, null=True)
    file = models.FileField(upload_to='books/%Y-%m-%d/')
    original_name = models.CharField(max_length=255, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.original_name and self.file:  # Сохраняем оригинальное имя при первом сохранении
            self.original_name = self.file.name
        super().save(*args, **kwargs)
    
    def get_original_filename(self):
        return os.path.basename(self.original_name) if self.original_name else "Файл"
    
    def __str__(self):
        return self.get_original_filename()
    
    class Meta:
        verbose_name = 'Материал к разделу советы и рекомендации'
        verbose_name_plural = 'Материалы к разделу советы и рекомендации'

    
class TestNew(models.Model):
    title = models.CharField('Название теста', max_length=100)
    description = RichTextField("Описание", blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

class QuestionNew(models.Model):
    test = models.ForeignKey(TestNew, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Текст вопроса', max_length=255)

class AnswerOptionNew(models.Model):
    question = models.ForeignKey(QuestionNew, on_delete=models.CASCADE, related_name='options')
    text = models.CharField('Вариант ответа', max_length=100)
    points = models.IntegerField('Баллы')

    def __str__(self):
        return f"{self.text} ({self.points} баллов)"
    
class Criterion(models.Model):
    test = models.ForeignKey(TestNew, on_delete=models.CASCADE, related_name='criteria')
    min_score = models.IntegerField()
    max_score = models.IntegerField()
    result_text = models.TextField('Результат')

    class Meta:
        ordering = ['min_score']

    class Meta:
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'