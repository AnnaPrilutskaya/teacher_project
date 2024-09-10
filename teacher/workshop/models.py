from django.db import models

class Documents(models.Model):
    """Класс тегов."""
    '''word = models.CharField(max_length=200,
                            verbose_name='Текстовый документ',
                            unique=True)'''
    title = models.CharField('Название', max_length=50, default='name') 
    word = models.FileField(upload_to='books/%Y-%m-%d/')

    # Не знаю, писать этот метод тут или в Activities
    def display_text_file(self):
        with open(self.word.path) as fp:
            return fp.read().replace('\n', '<br>')
        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'

class Activities(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.ManyToManyField(Documents, verbose_name='Текстовые документы', related_name='Acti',)
    '''music = 
    presentation = 
    video = '''

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Материал к разделу внеурочная деятельность'
        verbose_name_plural = 'Материалы к разделу внеурочная деятельность'

