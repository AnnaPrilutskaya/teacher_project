from django.db import models

class Documents(models.Model):
    """Класс тегов."""
    '''word = models.CharField(max_length=200,
                            verbose_name='Текстовый документ',
                            unique=True)'''
    title = models.CharField('Название', max_length=50, default='name') 
    word = models.FileField(upload_to='books/%Y-%m-%d/')

    # Не знаю, писать этот метод тут или в Activities
    '''def display_text_file(self):
        with open(self.word.path) as fp:
            return fp.read().replace('\n', '<br>')'''
        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Материал к разделу внеурочная деятельность'
        verbose_name_plural = 'Материалы к разделу внеурочная деятельность'

class Activities(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.ManyToManyField(Documents, verbose_name='Текстовые документы', related_name='Acti', blank=True, null=True)
    '''music = 
    presentation = 
    video = '''

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Внеурочная деятельность'
        verbose_name_plural = 'Внеурочная деятельность'


class Documents_for_measuring_materials(models.Model):
    """Класс тегов."""
    title = models.CharField('Название', max_length=50, default='name') 
    document = models.FileField(upload_to='books/%Y-%m-%d/')
        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Материал к разделу измерительные материалы'
        verbose_name_plural = 'Материалы к разделу измерительные материалы'

class Measuring_materials(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=1000, null=True, blank=True)
    materials = models.ManyToManyField(Documents_for_measuring_materials,
                                       verbose_name='Материалы',
                                       related_name='Measuring',
                                       blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Измерительный материал'
        verbose_name_plural = 'Измерительные материалы'