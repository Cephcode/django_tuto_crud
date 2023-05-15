from django.db import models

# Create your models here.
class Note(models.Model):
    content=models.CharField(max_length=400)
    completed=models.BooleanField(default=False)
     
    def __str__(self):
        return self.content