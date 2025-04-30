from django.db import models
from ckeditor.fields import RichTextField


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Запись для учеников'
        verbose_name_plural = 'Записи для учеников'

class Memos(models.Model):
    title = models.CharField('Название', max_length=50)
    content = RichTextField("Текст", blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Памятка для учеников'
        verbose_name_plural = 'Памятки для учеников'


class Recommendations(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Текст')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Совет и рекомендация для учеников'
        verbose_name_plural = 'Советы и рекомендации для учеников'

