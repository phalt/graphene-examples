from django.db import models


class BookModel(models.Model):
    name = models.CharField(max_length=100)