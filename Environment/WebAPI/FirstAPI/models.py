from django.db import models
from django.db.models.fields import BinaryField

# Create your models here.
class Person(models.Model):
    Name= models.CharField(max_length=50) 
    BirthDay = models.DateTimeField()
    Age = models.IntegerField()
    
    def __str__(self):
        return self.Name