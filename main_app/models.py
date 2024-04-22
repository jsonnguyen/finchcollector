from django.db import models

# Create your models here.
class Finch(models.Model):
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
            return self.type