from django.contrib import admin
from .models import Documents, Activities, Documents_for_measuring_materials, Measuring_materials
#from django_multiupload.admin import MultiUploadAdmin

'''class DocumentsAdmin(MultiUploadAdmin):
    multiupload_form = True  # Включаем множественную загрузку в форме
    multiupload_list = False  # Отключаем в списке (если не нужно)'''

# Register your models here.
admin.site.register(Documents)
admin.site.register(Activities)
admin.site.register(Documents_for_measuring_materials)
admin.site.register(Measuring_materials)