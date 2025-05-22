from django.db import models
import os
from ckeditor.fields import RichTextField

class Documents(models.Model):
    """Класс тегов."""
    
    activity = models.ForeignKey(
        'Activities',
        on_delete=models.CASCADE,
        related_name='files',
        null=True,  
        blank=True
    )
    file = models.FileField(upload_to='books/%Y-%m-%d/', null=True, blank=True)
    original_name = models.CharField(max_length=255, blank=True, null=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.original_name and self.file:  # Сохраняем оригинальное имя при первом сохранении
            self.original_name = self.file.name
        super().save(*args, **kwargs)
    
    def get_original_filename(self):
        return os.path.basename(self.original_name) if self.original_name else "Файл"
    
    def __str__(self):
        return self.get_original_filename()

    

    class Meta:
        verbose_name = 'Материал к разделу внеурочная деятельность'
        verbose_name_plural = 'Материалы к разделу внеурочная деятельность'

class Activities(models.Model):
    title = models.CharField('Название', max_length=50)
    content = RichTextField("Текст с форматированием", blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Внеурочная деятельность'
        verbose_name_plural = 'Внеурочная деятельность'


class Documents_for_measuring_materials(models.Model):
    """Класс тегов."""

    measuring_material = models.ForeignKey(
        'Measuring_materials', 
        on_delete=models.CASCADE, 
        related_name='files',
        null=True,  
        blank=True
    )
    file = models.FileField(upload_to='books/%Y-%m-%d/', null=True, blank=True)
    original_name = models.CharField(max_length=255, blank=True, null=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.original_name and self.file:  # Сохраняем оригинальное имя при первом сохранении
            self.original_name = self.file.name
        super().save(*args, **kwargs)
    
    def get_original_filename(self):
        return os.path.basename(self.original_name) if self.original_name else "Файл"
    
    def __str__(self):
        return self.get_original_filename()

    class Meta:
        verbose_name = 'Материал к разделу измерительные материалы'
        verbose_name_plural = 'Материалы к разделу измерительные материалы'

class Measuring_materials(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=1000, null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Измерительный материал'
        verbose_name_plural = 'Измерительные материалы'

class Lessons(models.Model):
    title = models.CharField('Название', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.TextField('Предмет', blank=True, null=True)
    class_number = models.TextField('Класс', blank=True, null=True)
    program = models.TextField('Программа', blank=True, null=True)
    topic = models.TextField('Тема', blank=True, null=True)
    lesson_type = models.TextField('Тип урока', blank=True, null=True)
    goal = models.TextField('Цель', blank=True, null=True)
    tasks = models.TextField('Задачи', blank=True, null=True)
    equipment = models.TextField('Оборудование', blank=True, null=True)
    content = RichTextField("Текст с форматированием", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class Files_for_lesson(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='files')
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
        verbose_name = 'Материал к разделу уроки'
        verbose_name_plural = 'Материалы к разделу уроки'