from django.db import models


# Create your models here.
class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(unique=True, max_length=100)
    def __str__(self):
        return f"Author: {self.author_name}, id: {self.author_id}"
