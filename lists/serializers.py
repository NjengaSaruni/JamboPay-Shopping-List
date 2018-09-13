from rest_framework.serializers import ModelSerializer

from lists.models import Item, ShoppingList


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ShoppingListSerializer(ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = '__all__'
