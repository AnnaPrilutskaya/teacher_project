# Generated by Django 4.2.1 on 2025-04-28 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0011_lessons_archive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessons',
            name='archive',
        ),
    ]
