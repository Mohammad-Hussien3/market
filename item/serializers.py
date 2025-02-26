from rest_framework import serializers
from .models import Category, Item, Order, PackageItem, Package


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

        
class LimitedCategorySerializer(serializers.ModelSerializer):
    limited_student_items = ItemSerializer(many=True, read_only=True)
    limited_doctor_items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'


class PackageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageItem
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'name']