from django.db import models

# Create your models here.

class Book(models.Model):
    Title = models.CharField(max_length=40)
    Author = models.CharField(max_length=40)
    Subject = models.CharField(max_length=40)
    def __str__(self):
        return self.Title + " " + self.Author