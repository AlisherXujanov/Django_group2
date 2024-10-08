# Generated by Django 5.1.1 on 2024-10-08 12:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название задачи', max_length=50)),
                ('description', models.TextField(help_text='Описание задачи')),
                ('deadline', models.CharField(help_text='Дедлайн задачи (время выполнения)', max_length=20)),
                ('completed', models.BooleanField(default=False, help_text='Статус задачи (выполнена/нет)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('color', models.CharField(default='black', help_text='Цвет текста задачи', max_length=20)),
                ('background_color', models.CharField(default='#f8f9fa', help_text='Цвет фона задачи', max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
                'ordering': ['-created_at'],
            },
        ),
    ]
