from django.db import models

# Create your models here.
class TODOLIST(models.Model):
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.task 
    
class History(models.Model):
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __srt__(self):
        return self.task
    
