from django import forms
from .models import Note

# forms.py
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Название заметки'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 4
            })
        }

