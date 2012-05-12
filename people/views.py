# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from yak.people.models import Person, Note, Tag

@login_required
def allpeople(request):
    return render_to_response('people/allpeople.html', {'people': Person.objects.all().order_by('name')})

@login_required
def allnotes(request):
    return render_to_response('people/allnotes.html', {'notes': Note.objects.all().order_by('-date')})

@login_required
def alltags(request):
    return render_to_response('people/alltags.html', {'tags': Tag.objects.all().order_by('text')})

@login_required
def person(request, id):
    person = Person.objects.get(id = id)
    return render_to_response('people/person.html', {'person' : person})

@login_required
def note(request, id):
    note = Note.objects.get(id = id)
    return render_to_response('people/note.html', {'note' : note})

@login_required
def tag(request, text):
    tag = Tag.objects.get(text = text)
    return render_to_response('people/tag.html', {'tag' : tag})


