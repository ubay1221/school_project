from django.db import models


class Group(models.Model):
    g_name = models.CharField(max_length=100)
    g_type = models.CharField(max_length=100)

