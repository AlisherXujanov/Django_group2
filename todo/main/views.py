from django.shortcuts import render
from .models import Todos


# CRUD - Create, Read, Update, Delete


# Create your views here.
def home_page(request):
    todos = Todos.objects.all()

    context = {
        "title": "Welcome to the Home Page",
        "todo": todos.first()
    }
    return render(request, 'home.html', context)


def about_page(request):
    context = {
        "title": "Welcome to the About Page",
    }
    return render(request, 'about.html', context)