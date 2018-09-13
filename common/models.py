# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    price = models.DecimalField(blank=True, default=0.0, decimal_places=2, max_digits=100)
    size = models.DecimalField(blank=True, null=True, default=1.00, decimal_places=2, max_digits=100)
    unit = models.CharField(null=True, blank=True, max_length=255)

    def __unicode__(self):
        if not self.unit:
            self.unit = ''

        return '{} {} x {} - Kshs {}'.format(
            self.size,
            self.unit,
            self.name,
            self.price
        )
