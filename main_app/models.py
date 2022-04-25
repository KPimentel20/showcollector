from django.db import models

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