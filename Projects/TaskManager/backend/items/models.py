from django.db import models

# Create your models here.

# row in db for an item
class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    container = models.CharField(max_length=50)

