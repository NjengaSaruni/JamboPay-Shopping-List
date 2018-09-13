from rest_framework.serializers import ModelSerializer

from lists.models import Item, ShoppingList, ShoppingItem


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


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
