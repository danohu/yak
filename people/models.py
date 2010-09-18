from django.db import models
import datetime


# Create your models here.

class Person(models.Model):
    tags = models.ManyToManyField('Tag', related_name = 'people')
    name = models.CharField(max_length = 50)
    contact_details = models.TextField(blank = True)
    description = models.TextField(blank = True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'
        ordering = ('name',)


class Note(models.Model):
    date = models.DateTimeField('date written', default = datetime.datetime.now)
    people = models.ManyToManyField('Person', related_name = 'notes')
    title = models.CharField(max_length = 200, default = None)
    text = models.TextField(blank = True)
    tags = models.ManyToManyField('Tag', related_name = 'notes')

    def __unicode__(self):
        return self.title or ''

    class Meta:
        ordering = ('-date', 'title')

class Tag(models.Model):
    text = models.CharField(max_length = 50, unique = True)

    def __unicode__(self):
        return self.text
    
    class Meta:
        ordering = ('text',)

