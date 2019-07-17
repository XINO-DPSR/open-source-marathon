from __future__ import unicode_literals

from django.db import models


class search_database(models.Model):
    query = models.CharField(max_length=128)

    def __str__(self):
        return self.query
