from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    how_known = models.CharField(max_length=100, blank=True)
    comment = models.TextField(blank=True)