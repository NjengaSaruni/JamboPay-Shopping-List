# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from common.models import Item


class AbstractBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    shopper = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class ShoppingList(AbstractBase):
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    budget = models.DecimalField(blank=True, default=0.0, decimal_places=2, max_digits=100)
    limit = models.DecimalField(blank=True, default=0.0, decimal_places=2, max_digits=100)

    def get_total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price

        return total

    total = property(get_total_price)

    def get_total_bought(self):
        total = 0
        for item in self.items.filter(bought=True):
            total += item.price

        return total

    total_bought = property(get_total_bought)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.limit >= self.budget:
            raise ValidationError('Budget limit cannot be bigger or equal to budget')

        return super(ShoppingList, self).save()

    def __unicode__(self):
        return '{} - {} <> {}'.format(
            self.name,
            self.total,
            self.budget
        )


class ShoppingItem(AbstractBase):
    item = models.ForeignKey(Item)
    quantity = models.IntegerField(default=1, blank=True)
    list = models.ForeignKey(ShoppingList, related_name='items')
    bought = models.BooleanField(default=False, blank=True)

    def get_total_price(self):
        return self.item.price * self.quantity

    price = property(get_total_price)

    def __unicode__(self):
        return '{} x {} in {} @ {}'.format(
            self.quantity,
            self.item.name,
            self.list.name,
            self.price
        )


# method for updating
@receiver(post_save, sender=ShoppingItem, dispatch_uid="update_budget")
def update_budget(sender, instance, **kwargs):
    if instance.bought:
        instance.list.budget -= instance.price
    else:
        instance.list.budget += instance.price

    instance.list.save()
