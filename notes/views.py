from django.shortcuts import render,redirect
from .models import Note
from .forms import NoteForm



def note_list(request):
    notes = Note.objects.all()  # Запрос к БД
    return render(request, 'notes/list.html', {'notes': notes})


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')  # Перенаправляем на список заметок
    else:
        form = NoteForm()  # Пустая форма для GET-запроса
    return render(request, 'notes/add_note.html', {'form': form})

