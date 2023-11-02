from django.db import models

# Create your models here.

class Comment(models.Model):
   name = models.TextField()
   text = models.TextField()