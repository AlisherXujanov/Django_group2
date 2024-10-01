from django.shortcuts import render, redirect
from .models import Todos
from .forms import TodoForm
from django.contrib import messages


# Create your views here.
def home_page(request):
    todos = Todos.objects.all()

    context = {
        "title": "Welcome to the Home Page",
        "todos": todos.order_by("-created_at")
    }
    return render(request, 'home.html', context)


def about_page(request):
    context = {
        "title": "Welcome to the About Page",
    }
    return render(request, 'about.html', context)


# CRUD - Create, Read, Update, Delete
def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo created successfully")
            return redirect("home")


    form = TodoForm()
    context = {
        "title": "Create a new Todo",
        "form": form
    }
    return render(request, "create_todo.html", context)