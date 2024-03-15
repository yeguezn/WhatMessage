from django.db import models
from categories.models import Category

# Create your models here.

class GenericMessage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    content = models.CharField(max_length=150)

    def __str__(self):
        return self.content
    

