# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from common.mixins import GetQuerysetMixin
from lists.models import ShoppingList, ShoppingItem
from lists.serializers import ShoppingListSerializer, ShoppingItemSerializer


class ShoppingListListCreateView(generics.ListCreateAPIView):
    serializer_class = ShoppingListSerializer
    queryset = ShoppingList.objects.all()

    search_fields = (
        'items',
    )

    def create(self, request, *args, **kwargs):
        request.data['shopper'] = request.user.id

        return super(ShoppingListListCreateView, self).create(request);


class ShoppingListDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShoppingListSerializer
    queryset = ShoppingList.objects.all()


class ShoppingItemListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = ShoppingItemSerializer
    queryset = ShoppingItem.objects.all()
    search_fields = [
        'item__name', 'item__price'
    ]


class ShoppingItemDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShoppingItemSerializer
    queryset = ShoppingItem.objects.all()
