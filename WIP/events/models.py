from django.db import models
from django.utils import timezone

class Event(models.Model):

    eventType = models.CharField(max_length=200)
    eventName = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    eventScope = models.CharField(max_length=200)
    dateCreated = models.DateTimeField('Date Created')
    dateActive = models.DateTimeField('Date Active')
    recurrence = models.CharField(max_length=200)

    def __str__(self):
        return self.eventName

    def is_active(self):
        return self.dateActive >= timezone.now() \
            - datetime.timedelta(seconds=1)