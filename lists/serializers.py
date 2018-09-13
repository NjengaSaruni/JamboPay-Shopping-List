from rest_framework.serializers import ModelSerializer

from common.serializers import ItemSerializer
from lists.models import ShoppingList, ShoppingItem


class ShoppingItemSerializer(ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = ShoppingItem
        fields = '__all__'


class ShoppingListSerializer(ModelSerializer):
    items = ShoppingItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = '__all__'
