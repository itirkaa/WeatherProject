from django.db import models

# Create your models here.
"""
This will create a table in our database that will have a column called name and id
"""
class City(models.Model):
    name = models.CharField(max_length=30)
    
    def _str_(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'cities'

class Feedback(models.Model):
    name  = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    feedback = models.TextField(null=False, blank=False)
    
    
class Message(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    message = models.TextField(null=False, blank=False)