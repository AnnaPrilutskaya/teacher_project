# Generated by Django 4.2.1 on 2025-04-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0007_documents_for_measuring_materials_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activities',
            options={'verbose_name': 'Внеурочная деятельность', 'verbose_name_plural': 'Внеурочная деятельность'},
        ),
        migrations.AlterModelOptions(
            name='documents',
            options={'verbose_name': 'Материал к разделу внеурочная деятельность', 'verbose_name_plural': 'Материалы к разделу внеурочная деятельность'},
        ),
        migrations.AlterModelOptions(
            name='documents_for_measuring_materials',
            options={'verbose_name': 'Материал к разделу измерительные материалы', 'verbose_name_plural': 'Материалы к разделу измерительные материалы'},
        ),
        migrations.AlterModelOptions(
            name='measuring_materials',
            options={'verbose_name': 'Измерительный материал', 'verbose_name_plural': 'Измерительные материалы'},
        ),
        migrations.AddField(
            model_name='measuring_materials',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
    ]
