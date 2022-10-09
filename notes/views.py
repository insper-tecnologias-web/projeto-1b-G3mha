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
    new_quantity = int(quantity)
    new_quantity = int(quantity) - 1
    if new_quantity < 0:
        new_quantity = 0
    print('#' * 50)
    Cadastro.objects.filter(name=name).update(quantity=new_quantity)
    return redirect('index')
