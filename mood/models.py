from django.db import models
import datetime


# Create your models here.

class Aspect(models.Model):
    name = models.CharField(max_length = 20, unique = True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Snapshot(models.Model):
    date = models.DateTimeField(default = datetime.datetime.now)

    def __unicode__(self):
        return self.date.strftime('%F')

    class Meta:
        ordering = ('-date',)

class Ranking(models.Model):
    aspect = models.ForeignKey('Aspect')
    snapshot = models.ForeignKey('Snapshot')
    score = models.IntegerField() #XXX: how to specify max/min? [out of 100]

    def __unicode__(self):
        return '%s:%s' % (self.aspect, self.snapshot)


