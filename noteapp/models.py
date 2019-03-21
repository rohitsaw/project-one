from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    heading = models.CharField(max_length=100)
    notes = models.TextField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.user.name}-{self.heading}"
