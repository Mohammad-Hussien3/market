from rest_framework import serializers
from .models import Category, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

        
class LimitedCategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, source='limited_items')
    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'
