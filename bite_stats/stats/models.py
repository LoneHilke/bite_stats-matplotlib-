from django.db import models

# Create your models here.
class BiteStat(models.Model):
    exercise = models.PositiveSmallIntegerField()  # 0 to 32767
    completed = models.DateField()  # I don't care about time here
    level = models.PositiveSmallIntegerField(null=True, blank=True)  # optional, not every Bite has user feedback 