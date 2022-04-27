from django.db import models
from django.urls import reverse

# Create your models here.
class Show(models.Model): # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    releaseyear = models.IntegerField()

releaseyear = models.IntegerField()
    # new code below

def __str__(self):
        return self.name

def get_absolute_url(self):

    return reverse('detail', kwargs={'show_id': self.id})


# A tuple of 2-tuples
CHANNELS = (
    ('H', 'HBO MAX'),
    ('N', 'Netflix'),
    ('D', 'Disney +'),
)

class StreamingService(models.Model):
    date = models.DateField('watch date')
    channel = models.CharField(
        max_length=1,
        choices=CHANNELS,
        default=CHANNELS[0][0]
    )


# new code above
show = models.ForeignKey(Show, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.get_channel_display()} on {self.date}"

class Meta:
    ordering = ['-date']
