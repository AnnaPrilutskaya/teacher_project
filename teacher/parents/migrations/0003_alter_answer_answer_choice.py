# Generated by Django 4.2.1 on 2025-04-30 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0002_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_choice',
            field=models.CharField(choices=[('yes', 'Да'), ('no', 'Нет'), ('dont_know', 'Иногда')], max_length=20),
        ),
    ]
