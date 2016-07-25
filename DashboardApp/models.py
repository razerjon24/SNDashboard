from __future__ import unicode_literals
from django.db import models
# Create your models here.

class Points(models.Model):
    day = models.IntegerField(default=0)
    hour = models.IntegerField(default=0)
    lat = models.TextField()
    lon = models.TextField()
    def __unicode__(self):
        return "%s,%s"%(self.lon,self.lat)

class Bursts(models.Model):
    topic = models.TextField()
    level = models.IntegerField()
    day = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    def __unicode__(self):
        return "%s,%s"%(self.topic,self.level)

class Clusters(models.Model):
    cluster = models.IntegerField()
    lon = models.TextField()
    lat = models.TextField()
    tipo = models.TextField()
    def __unicode__(self):
        return "%s,%s"%(self.lon,self.lat)

class Pics(models.Model):
    url = models.TextField()
    cluster = models.IntegerField()
    tipo = models.TextField()
