from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page, name="home"),
    path("about/", about_page, name="about"),
    path("create-todo/", create_todo, name="create_todo"),
    path("todo-details/<int:pk>", todo_details, name="todo_details"),
]
