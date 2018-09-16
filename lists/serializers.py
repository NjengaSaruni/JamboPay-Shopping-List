from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from common.mixins import AbstractFieldsMixin
from common.serializers import ItemSerializer
from lists.models import ShoppingList, ShoppingItem


class ShoppingItemSerializer(ModelSerializer):
    price = serializers.ReadOnlyField()
    item = ItemSerializer(read_only=True)

    class Meta:
        model = ShoppingItem
        fields = '__all__'


class ShoppingItemInlineSerializer(ModelSerializer):
    item = ItemSerializer(read_only=True)
    price = serializers.ReadOnlyField()

    class Meta:
        model = ShoppingItem
        fields = '__all__'


class ShoppingListSerializer(ModelSerializer):
    items = ShoppingItemInlineSerializer(many=True, read_only=True)
    total = serializers.ReadOnlyField()
    total_bought = serializers.ReadOnlyField()

    def create(self, validated_data):
        print validated_data

        return super(ShoppingListSerializer, self).create(validated_data)


    class Meta:
        model = ShoppingList
        fields = '__all__'
