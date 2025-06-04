from rest_framework import serializers
from .models import Category, Item, Order, Package, PointItem, OrderItem, OrderPointItem, OrderPackage, GlobalPoints


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ('created_at',)


class PointItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointItem
        exclude = ('created_at',)


class LimitedCategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)

        if not data.get('items'):
            data.pop('items', None)

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
        representation['price'] = instance.item.price
        representation['photo'] = instance.item.photo.url
        return representation


class OrderPointItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPointItem
        fields = ['quantity']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['point_item_name'] = instance.point_item.name
        representation['points'] = instance.item.points
        representation['photo'] = instance.item.photo.url
        return representation
    
    
class OrderPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPackage
        fields = ['quantity']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['package_name'] = instance.package.name
        return representation


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='orderitem_set', many=True)
    point_items = OrderPointItemSerializer(source='orderpointitem_set', many=True)
    packages = OrderPackageSerializer(source='orderpackage_set', many=True)

    class Meta:
        model = Order
        fields = ['id', 'profile', 'status', 'created_at', 'items', 'purchased_at', 'point_items', 'packages', 'active_type', 'customer_info']

    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if instance.active_type == 'price':
            representation['price'] = instance.total_price
        elif instance.active_type == 'point':
            representation['points'] = instance.total_points


        return representation
    

class GlobalPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalPoints
        fields = ['referral_points', 'purchase_points', 'referral_purchase_points']