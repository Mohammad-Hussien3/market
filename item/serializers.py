from rest_framework import serializers
from .models import Category, Item, Order, PackageItem, Package


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ('created_at',)

        
class LimitedCategorySerializer(serializers.ModelSerializer):
    limited_student_items = ItemSerializer(many=True, read_only=True)
    limited_doctor_items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)

        if not data.get('limited_student_items'):
            data.pop('limited_student_items', None)
        if not data.get('limited_doctor_items'):
            data.pop('limited_doctor_items', None)

        return data


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'

    
class NewCategorySerializer(serializers.ModelSerializer):
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
        fields = '__all__'