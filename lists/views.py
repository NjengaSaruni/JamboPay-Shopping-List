# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from lists.models import ShoppingList, ShoppingItem
from lists.serializers import ShoppingListSerializer, ShoppingItemSerializer


class ShoppingListListCreateView(generics.ListCreateAPIView):
    serializer_class = ShoppingListSerializer
    queryset = ShoppingList.objects.all()


class ShoppingListDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShoppingListSerializer
    queryset = ShoppingList.objects.all()


class ShoppingItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ShoppingItemSerializer
    queryset = ShoppingItem.objects.all()


class ShoppingItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShoppingItemSerializer
    queryset = ShoppingItem.objects.all()

