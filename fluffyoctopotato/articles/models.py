from django.db import models


# Create your models here.
class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    author_name = models.CharField(unique=True, max_length=100)
