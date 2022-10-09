from django.shortcuts import render, redirect
from .models import Note

# CRUD - Create, Read, Update, Delete

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        note_id = request.POST.get('id')
        if 'criar' in request.POST:
            note = Note.objects.create(title=title, content=content, tag=tag)
            note.save()
        if 'editar' in request.POST:
            return redirect(f'update/{note_id}')
        if 'deletar' in request.POST:
            try:
                note_selected = Note.objects.get(id=int(note_id))
                note_selected.delete()
            except Note.DoesNotExist:
                pass
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def update(request):
    note_id = request.POST.get('id')
    if (request.method == 'POST') and ('alterado' in request.POST):
        note_selected = Note.objects.get(id=int(note_id))
        title = request.POST.get('title')
        if not(title == ''):
            note_selected.update(title=title)
        content = request.POST.get('content')
        if not(content == ''):
            note_selected.update(content=content)
        tag = request.POST.get('tag')
        if not(tag == ''):
            note_selected.update(tag=tag)
        return redirect('index')
    else:
        note_selected = Note.objects.filter(id=int(note_id))
        return render(request, 'notes/update.html', {'notes': note_selected})
