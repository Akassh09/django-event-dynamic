from django.db import models

# Create your models here.

class Event(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    loc = models.TextField()
    date = models.DateField(auto_now_add=False, blank=True)
    time = models.TimeField(auto_now_add=False, blank=True)
    liked = models.BooleanField(default=False)

    def __str__(self): 
        return self.name
    