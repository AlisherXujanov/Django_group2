from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {
        "title": "Welcome to the Home Page"
    }
    return render(request, 'home.html', context)