from rest_framework.serializers import ModelSerializer

from common.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemInlineSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'price']
