from django.db import models

# Create your models here.

class Other(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название категории
    description = models.TextField(blank=True, null=True)  # Описание категории

    def __str__(self):
        return self.name
