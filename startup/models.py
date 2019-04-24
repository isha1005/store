from django.db import models
from django.contrib.auth.models import User


class About(models.Model):
    title = models.CharField(max_length=200, null=False, unique=True)
    body_block = models.TextField(max_length=5000, null=True, blank=True)


class FAQ(models.Model):
    title = models.CharField(max_length=200, null=False, unique=True)
    block_body = models.TextField(max_length=5000, null=True, blank=True)
