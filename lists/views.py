# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from lists.models import ShoppingList
from lists.serializers import ShoppingListSerializer


class ShoppingListListCreateView(generics.ListCreateAPIView):
    serializer_class = ShoppingListSerializer
    queryset = ShoppingList.objects.all()
