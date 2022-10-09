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
    note_selected = Note.objects.get(id=int(note_id))
    if (request.method == 'POST') and ('alterado' in request.POST):
        Note.objects.filter(name=name).update(quantity=new_quantity) # TODO
    else:
        note_selected = Note.objects.filter(id=int(note_id))
        return render(request, 'notes/update.html', {'notes': note_selected})

    return redirect('index')
