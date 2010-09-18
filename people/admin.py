from yak.people.models import Person, Tag, Note
from django.contrib import admin

class NoteInline(admin.StackedInline):
    model = Note
    extra = 2

class TagInline(admin.TabularInline):
    model = Tag
    extra = 2

class PersonAdmin(admin.ModelAdmin):
    pass
    """the only way of getting inline M2M fields in django admin is thru
    odd little hacks -- see 
    http://www.djangosnippets.org/snippets/1295/http://www.djangosnippets.org/snippets/1295/
    """
    #inlines = [TagInline]

admin.site.register(Person, PersonAdmin)
admin.site.register(Tag)
admin.site.register(Note)

