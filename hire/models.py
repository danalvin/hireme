from django.db import models
from django.utils import timezone

from accounts.models import User
# Create your models here.

Event_type = (
    ('1', "Wedding"),
    ('2', "Birthday"),
    ('3', "Chama"),
    ('4', "Any other")
)

Event_size = (
    ('1', "0-50"),
    ('2', "50-100"),
    ('3', "100-200"),
    ('4', "200+")
)

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    location = models.CharField(max_length=100)
    cake = models.BooleanField(default=False)
    event_size = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    last_date = models.DateTimeField()
    resources = models.CharField(max_length=1000, help_text="Example, chairs, tents. Separate with a comma" )
    AoB = models.CharField(help_text="Anything you should let us know, include it here?", max_length=2000)

    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})

class resources(models.Model):
    tables = models.NullBooleanField(null=True)