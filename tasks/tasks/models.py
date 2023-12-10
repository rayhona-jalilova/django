from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    description = models.TextField()