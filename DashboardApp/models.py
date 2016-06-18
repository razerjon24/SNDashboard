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