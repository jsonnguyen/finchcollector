from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
            return self.type

    def get_absolute_url(self):
        return reverse("detail", kwargs={"finch_id": self.id})
    
class Feeding(models.Model):
    MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner')
    )
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default='B')
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    
    class Meta:
        ordering = ('-date',)
    