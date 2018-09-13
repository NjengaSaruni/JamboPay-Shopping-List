# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.conf import settings
from django.db import models


# Create your models here.

class AbstractBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    shopper = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    price = models.DecimalField(blank=True, default=0.0, decimal_places=2, max_digits=100)


class ShoppingList(AbstractBase):
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    budget = models.DecimalField(blank=True, default=0.0, decimal_places=2, max_digits=100)


class ShoppingItem(AbstractBase):
    item = models.ForeignKey(Item)
    quantity = models.IntegerField(default=1, blank=True)
    list = models.ForeignKey(ShoppingList, related_name='items')

    def get_total_price(self):
        return self.item.price * self.quantity

    price = property(get_total_price)
