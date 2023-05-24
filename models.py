from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()

class Setting(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)