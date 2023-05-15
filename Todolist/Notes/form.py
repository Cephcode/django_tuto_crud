from django import forms
from django.forms import ModelForm
from .models import Note

class notes_form(ModelForm):
    class Meta:
        model = Note
        fields= ['content']
class finishNote(ModelForm):
    class Meta:
        model = Note
        fields= ['completed']