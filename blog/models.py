from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

# The model for the Location table
class Location(models.Model):
    l_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    l_name = models.CharField(max_length = 100)
    x_cord = models.FloatField() 
    y_cord = models.FloatField() 
    description = models.TextField()
    times_cleaned = models.IntegerField() 

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk':self.pk})

# The model for the Cleaned table
class Cleaned(models.Model):
    l_id = models.ForeignKey(Location, on_delete = models.CASCADE)
    u_id = models.ForeignKey(User, on_delete = models.CASCADE)
    date_cleaned = models.DateTimeField(default = timezone.now)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.l_id.l_id})
