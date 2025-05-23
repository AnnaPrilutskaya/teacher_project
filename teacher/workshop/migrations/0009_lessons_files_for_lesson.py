# Generated by Django 4.2.1 on 2025-04-25 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0008_alter_activities_options_alter_documents_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='Files_for_lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='books/%Y-%m-%d/')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='workshop.lessons')),
            ],
            options={
                'verbose_name': 'Материал к разделу уроки',
                'verbose_name_plural': 'Материалы к разделу уроки',
            },
        ),
    ]
