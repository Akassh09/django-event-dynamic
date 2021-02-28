from django.db import models

# Create your models here.

class Event(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    loc = models.TextField()
    liked = models.BooleanField(default=False)

    