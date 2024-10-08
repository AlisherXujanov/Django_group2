from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=50, help_text="Название задачи") # Название задачи
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # Владелец задачи
    description = models.TextField(help_text="Описание задачи") # Описание задачи
    deadline = models.CharField(max_length=20, help_text="Дедлайн задачи (время выполнения)") # Дедлайн задачи (время выполнения)
    completed = models.BooleanField(default=False, help_text="Статус задачи (выполнена/нет)") # Статус задачи (выполнена/нет)
    # ------------------- Время создания и обновления задачи -------------------
    created_at = models.DateTimeField(auto_now_add=True) # Время создания задачи
    updated_at = models.DateTimeField(auto_now=True) # Время последнего обновления задачи
    # ------------------- Дополнительные поля -------------------
    color = models.CharField(max_length=20, default='black', help_text="Цвет текста задачи") # Цвет текста
    background_color = models.CharField(max_length=20, default='#f8f9fa', help_text="Цвет фона задачи") # Цвет фона


    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} of - {self.owner}. Deadline: {self.deadline}. Status: {self.completed}"