from django.urls import path
from .views import *

urlpatterns = [
    path("profile/<int:user_pk>", profile_page, name="profile_page"),
]
