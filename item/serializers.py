from rest_framework import serializers
from .models import Category, Item


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
