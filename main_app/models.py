from django.db import models


class ItemModel(models.Model):
    name = models.CharField(max_length=30)
