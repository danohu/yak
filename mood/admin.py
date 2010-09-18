from yak.mood.models import *
from django.contrib import admin

for table in (Aspect, Snapshot, Ranking):
    admin.site.register(table)
