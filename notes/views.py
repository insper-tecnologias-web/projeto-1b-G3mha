from django.shortcuts import render, redirect
from .models import Note

# CRUD - Create, Read, Update, Delete

def create(request):
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    note = Note.objects.create(title=title, content=content)
    note.save()
    return redirect('read')

def read(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': all_notes})

def update(request):
    pass # TODO: Implementar a função update

def delete(request, note_id):
    try:
        note_selected = Note.objects.get(id=int(note_id))
        note_selected.delete()
    except Note.DoesNotExist:
        pass
    return redirect('read')
