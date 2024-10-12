from .models import Profile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

def profile_page(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    profile = Profile.objects.get(user=user)
    context = {
        'profile': profile
    }
    return render(request, "profile.html", context)