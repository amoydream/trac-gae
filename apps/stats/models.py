from django.db import models
from trac.models import Athlete, Coach

class PerformanceRecord(models.Model):
    distance = models.IntegerField()
    time = models.FloatField()
    interval = models.CharField(max_length=1)
    VO2 = models.IntegerField(null=True, blank=True)
    athlete = models.ForeignKey(Athlete, null=True)
    coach = models.ForeignKey(Coach, null=True)

    def __unicode__(self):
        if self.athlete:
            name = self.athlete.user.username
        elif self.coach:
            name = self.coach.user.username
        else:
            name = ''
        return "user={}".format(name)
