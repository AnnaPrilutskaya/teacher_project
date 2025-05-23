# Generated by Django 4.2.1 on 2025-04-30 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0016_remove_documents_for_measuring_materials_document_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='workshop.activities'),
        ),
        migrations.AddField(
            model_name='documents',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='books/%Y-%m-%d/'),
        ),
        migrations.AddField(
            model_name='documents',
            name='original_name',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='documents',
            name='title',
            field=models.CharField(blank=True, default='name', max_length=50, null=True, verbose_name='Название'),
        ),
    ]
