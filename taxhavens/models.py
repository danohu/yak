from django.db import models

# Create your models here.

class JSONField(models.TextField):
    """XXX: create me, from http://code.djangoproject.com/attachment/ticket/12990/json_field.diff"""
    pass

class Person(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField()
    datasource = models.ForeignKey('DataSource')
    details = JSONField(blank = True, null = True)


class DataSource(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField()
    details = JSONField(blank = True, null = True)

class Entity(models.Model):
    """Entity can be a person or a company.
    This is a big improvement over the prior situation,where
    we had companies masquerading as people"""
    TYPE_CHOICES = (
            ('P', 'Person'),
            ('C', 'Company'),
            ('U', 'Unknown'))
    id = models.AutoField(primary_key = True)
    name = models.CharField()
    type = models.CharField(max_length = 1, choices = TYPE_CHOICES)
    datasource = models.ForeignKey('DataSource')
    details = JSONField(blank = True, null = True)

class Relationship(models.Model):
    agent = models.ForeignKey('Entity')
    victim = models.ForeignKeu('Entity')
    type = models.ForeignKey('RelationshipType')

class RelationshipType(models.Model):
    id = models.AutoField(primary_key = True)
    label = models.CharField()
    details = JSONField(blank = True, null = True)
