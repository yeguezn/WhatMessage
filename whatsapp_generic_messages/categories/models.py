from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name
