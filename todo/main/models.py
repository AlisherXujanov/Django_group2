from tabnanny import verbose
from django.db import models

# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=50) # Название задачи
    owner = models.CharField(max_length=50) # Владелец задачи
    description = models.TextField() # Описание задачи
    deadline = models.DateField() # Дедлайн задачи (время выполнения)
    completed = models.BooleanField(default=False) # Статус задачи (выполнена/нет)
    # ------------------- Время создания и обновления задачи -------------------
    created_at = models.DateTimeField(auto_now_add=True) # Время создания задачи
    updated_at = models.DateTimeField(auto_now=True) # Время последнего обновления задачи
    # ------------------- Дополнительные поля -------------------
    color = models.CharField(max_length=20, default='black') # Цвет задачи
    background_color = models.CharField(max_length=20, default='#f8f9fa') # Цвет фона задачи


    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} of - {self.owner}. Deadline: {self.deadline}. Status: {self.completed}"