from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Meeting(models.Model):
    meetingtype = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    meetingdate = models.DateField()
    meetingtime = models.TimeField()
    location = models.CharField(max_length=255)
    agenda = models.TextField()

    def __str__(self):
        return self.meetingtype

    class Meta:
        db_table = 'meeting'
        verbose_name_plural = 'meetings'


class Meeting_Minutes(models.Model):
    meetingId = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minute = models.TextField()

    class Meta:
        db_table = 'meeting minutes'
        verbose_name_plural = 'meeting minutes'


class Resource(models.Model):
    resourceName = models.CharField(max_length=255)
    resourceType = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    dateEntered = models.DateField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.resourceName

    class Meta:
        db_table = 'resource'
        verbose_name_plural = 'resources'


class Event(models.Model):
    eventTitle = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=255)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventTitle

    class Meta:
        db_table = 'event'
        verbose_name_plural = 'events'
