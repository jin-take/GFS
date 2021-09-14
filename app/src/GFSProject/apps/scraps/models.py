from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
import os.path

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):  # ...1
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=100, null=True, blank=True)
    date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)  # ...2
    tag = models.ManyToManyField(Tag, blank=True)  # ...3
    del_flag = models.BooleanField(default=False)  # ...4

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name