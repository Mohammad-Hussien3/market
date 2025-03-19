from rest_framework import serializers
from .models import Category, Item, Order, PackageItem, Package, PointItem, OrderItem, OrderPointItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ('created_at',)


class PointItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointItem
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


class PackageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageItem
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['quantity']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['item_name'] = instance.item.name
        return representation


class OrderPointItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPointItem
        fields = ['quantity']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['point_item_name'] = instance.point_item.name
        return representation
    
    


class OrderSerializer(serializers.ModelSerializer):
    item = OrderItemSerializer(source='orderitem_set', many=True)
    point_item = OrderPointItemSerializer(source='orderpointitem_set', many=True)
    package = PackageSerializer()

    class Meta:
        model = Order
        fields = ['id', 'profile', 'status', 'created_at', 'item', 'point_item', 'package', 'active_type']

    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if instance.active_type == 'item':
            representation['active'] = representation['item']
            representation['price'] = instance.total_price_items
        elif instance.active_type == 'point_item':
            representation['active'] = representation['point_item']
            representation['points'] = instance.total_points_items
        elif instance.active_type == 'package':
            representation['active'] = representation['package']['name']
            representation['price'] = representation['package']['price']

            
        del representation['item']
        del representation['point_item']
        del representation['package']

        return representation
