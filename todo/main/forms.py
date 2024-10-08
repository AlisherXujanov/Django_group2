from django import forms
from .models import Todos



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ["title", "description",  "deadline",  "color",  "background_color" ]




