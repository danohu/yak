# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

from yak.people.models import Person, Note, Tag

def allpeople(request):
    return render_to_response('people/allpeople.html', {'people': Person.objects.all().order_by('name')})

def allnotes(request):
    return render_to_response('people/allnotes.html', {'notes': Note.objects.all().order_by('-date')})

def alltags(request):
    return render_to_response('people/alltags.html', {'tags': Tag.objects.all().order_by('text')})

def person(request, id):
    person = Person.objects.get(id = id)
    return render_to_response('people/person.html', {'person' : person})

def note(request, id):
    note = Note.objects.get(id = id)
    return render_to_response('people/note.html', {'note' : note})

def tag(request, text):
    tag = Tag.objects.get(text = text)
    return render_to_response('people/tag.html', {'tag' : tag})


