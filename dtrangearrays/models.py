from datetime import timedelta
from django.db import models
from django.contrib.postgres.fields import ArrayField, DateTimeRangeField


class DateTimeRangeArray(models.Model):
    name = models.CharField(max_length=128)
    duration = DateTimeRangeField(null=True, blank=True)
    durations = ArrayField(
        DateTimeRangeField(
        ),
        blank=True,
        null=True
    )
