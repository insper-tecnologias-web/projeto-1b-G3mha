from email.policy import default
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Note
from .serializers import NoteSerializer

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
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

def update(request, note_id):
    if (request.method == 'POST') and ('alterado' in request.POST):
        title, content, tag = request.POST.get('title'), request.POST.get('content'), request.POST.get('tag')
        new_values = {}
        if not(title == ''):
            new_values['title'] = title
        if not(content == ''):
            new_values['content'] = content
        if not(tag == ''):
            new_values['tag'] = tag
        note_selected = Note.objects.get(id=int(note_id))
        for key, value in new_values.items():
            setattr(note_selected, key, value)
        note_selected.save()
        return redirect('index')
    else:
        note_selected = Note.objects.filter(id=int(note_id))
        return render(request, 'notes/update.html', {'notes': note_selected})

@api_view(['GET', 'POST'])
def api_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        new_note_data = request.data
        note.title = new_note_data['title']
        note.content = new_note_data['content']
        note.save()
    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)

@api_view(['GET', 'POST'])
def api_note(request):
    try:
        if request.method == 'POST':
            note_created = Note.objects.create(title=request.data['title'], content=request.data['content'])
            note_created.save()
        note = Note.objects.all()
    except Note.DoesNotExist:
        raise Http404()
    serializer = NoteSerializer(note, many=True)
    return Response(serializer.data)