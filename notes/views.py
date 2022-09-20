from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note.objects.create(title=title, content=content)
        if request.POST.__contains__('create'):
            note.save()
        
        if request.POST.__contains__('id'):
            note_delete_id = request.POST.get('id')
            note = Note(id=note_delete_id, title=title, content=content)
            if request.POST.__contains__('delete'):
                note.delete()
                
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})
