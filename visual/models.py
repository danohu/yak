from django.db import models
from datetime import date, datetime, timedelta
# Create your models here.


class RecurringTask(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 80, blank = True)
    description = models.CharField(max_length = 200, blank = True)
    max = models.IntegerField(null = True, blank = True, default = 1)

    def __unicode__(self):
        return self.name

class RecurringTaskResult(models.Model):
    task = models.ForeignKey('RecurringTask')
    date = models.DateField(default = datetime.now)
    result = models.IntegerField(null = True, blank = True, default = 0)
    comment = models.CharField(max_length = 200, null = True, blank = True) 

    def __unicode__(self):
        return '%s_%s' % (self.result, self.date.strftime('%F'))


class ActivityLog(models.Model):
    date = models.DateField(default = datetime.now)
    start = models.IntegerField(max_length = 4, null = True, blank = True)
    end = models.IntegerField(max_length = 4, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    #we want to have tags, but they can prob. be included
    #in the description
    
    def __unicode__(self):
        return self.description

    @classmethod
    def fixdates(self):
        """I don't want to type everything up for every item
        so instead have a function to match dates by order"""
        raise NotImplementedError

