from yak.visual.models import *
from django.contrib import admin

class RecurringTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'max')
    pass

class RecurringTaskResultAdmin(admin.ModelAdmin):
    list_display = ('task', 'date', 'result', 'comment')
    pass

class ActivityLogAdmin(admin.ModelAdmin):
    pass

admin.site.register(RecurringTask, RecurringTaskAdmin)
admin.site.register(RecurringTaskResult, RecurringTaskResultAdmin)
admin.site.register(ActivityLog, ActivityLogAdmin)
