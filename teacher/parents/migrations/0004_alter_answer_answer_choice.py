# Generated by Django 4.2.1 on 2025-04-30 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0003_alter_answer_answer_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_choice',
            field=models.CharField(choices=[('yes', 'Да'), ('no', 'Нет'), ('sometimes', 'Иногда')], max_length=20),
        ),
    ]
