from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from item.models import Category, Item, Package, Order, PointItem, OrderItem, OrderPointItem, OrderPackage, GlobalPoints
from item.serializers import ItemSerializer, PackageSerializer, NewCategorySerializer, CategorySerializer, OrderSerializer, PointItemSerializer, GlobalPointsSerializer
from rest_framework.views import Response, status
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import json
from usermanagament.models import Profile
from django.db import models

# Create your views here.

class CategoryItems(APIView):

    def get(self, request, id, item_type):
        category = get_object_or_404(Category, id=id)

        filtered_items = category.items.all().order_by('-created_at')

        return Response(ItemSerializer(filtered_items, many=True).data, status=status.HTTP_200_OK)


class GetItem(RetrieveAPIView):

    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_field = 'id'


class GetPointItem(RetrieveAPIView):

    serializer_class = PointItemSerializer
    queryset = PointItem.objects.all()
    lookup_field = 'id'


class GetPackage(RetrieveAPIView):

    serializer_class = PackageSerializer
    queryset = Package.objects.all()
    lookup_field = 'id'


class GetPackages(ListAPIView):

    serializer_class = PackageSerializer
    queryset = Package.objects.all()


class AllItems(ListAPIView):

    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        
        for item in response.data:
            item['category'] = Category.objects.get(id=item['category']).name
        
        return response


class CreateItem(CreateAPIView):
    serializer_class = ItemSerializer


class CreateCategory(CreateAPIView):
    serializer_class = NewCategorySerializer


class CreatePackage(CreateAPIView):
    serializer_class = PackageSerializer


class CreatePointItem(CreateAPIView):
    serializer_class = PointItemSerializer


class DeleteItem(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'


class DeletePointItem(DestroyAPIView):
    queryset = PointItem.objects.all()
    serializer_class = PointItemSerializer
    lookup_field = 'id'


class DeleteCategory(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class DeletePackage(DestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    lookup_field = 'id'


class UpdateItem(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'


class UpdatePointItem(UpdateAPIView):
    queryset = PointItem.objects.all()
    serializer_class = PointItemSerializer
    lookup_field = 'id'


class UpdateCategory(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = NewCategorySerializer
    lookup_field = 'id'


class UpdatePackage(UpdateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    lookup_field = 'id'


class GetPointItmes(ListAPIView):
    queryset = PointItem.objects.all()
    serializer_class = PointItemSerializer

    
class Search(APIView):

    def get(self, request, category_type, text):
        items = Item.objects.filter(name__icontains=text, category__category_type=category_type)
        return Response(ItemSerializer(items, many=True).data, status=status.HTTP_200_OK)
    

class SearchPackage(APIView):

    def get(self, request, text):
        items = Package.objects.filter(name__icontains=text)
        return Response(PackageSerializer(items, many=True).data, status=status.HTTP_200_OK)
    

class CreateOrder(APIView):

    def post(self, request):
        data = request.data
        profile_id = data['profile_id']
        profile = get_object_or_404(Profile, telegram_id=profile_id)

        order = Order.objects.create(
            profile=profile,
            active_type=data['active_type'],
            status='pending'
        )

        for item_data in data.get('items', []):
            item = get_object_or_404(Item, id=item_data['item_id'])
            OrderItem.objects.create(order=order, item=item, quantity=item_data['quantity'])

        for package_data in data.get('packages', []):
            package = get_object_or_404(Package, id=package_data['package_id'])
            OrderPackage.objects.create(order=order, package=package, quantity=package_data['quantity'])

        for point_item_data in data.get('point_items', []):
            point_item = get_object_or_404(PointItem, id=point_item_data['point_item_id'])
            OrderPointItem.objects.create(order=order, point_item=point_item, quantity=point_item_data['quantity'])

        order.update()
        address = data['address']
        phone_number = data['phone_number']
        name = data['name']

        order.customer_info = {
            'name':name,
            'phone_number':phone_number,
            'address':address
        }
        order.save()


        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class CategoryList(ListAPIView):
    serializer_class = NewCategorySerializer

    def get_queryset(self):
        return Category.objects.order_by(
            models.Case(
                models.When(category_type='student', then=0),
                models.When(category_type='doctor', then=1),
                output_field=models.IntegerField()
            ),
            '-created_at'
        )

    
class GetCategory(RetrieveAPIView):
    serializer_class = NewCategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'


class UpdateGlobalPointsView(UpdateAPIView):
    queryset = GlobalPoints.objects.all()
    serializer_class = GlobalPointsSerializer

    def get_object(self):
        return GlobalPoints.get_instance()
    

class GetOrders(APIView):

    def get(self, request, active_type):
        orders = Order.objects.filter(status__in=['delivery', 'pending'], active_type=active_type)
        jsonOrders = OrderSerializer(orders, many=True).data
        return Response(jsonOrders)


class GetOrder(RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'id'


class DeleteOrder(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'


class MakeOrderDelivery(APIView):

    def patch(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        order.status = 'delivery'
        order.save()
        return Response({'success':'success'}, status=status.HTTP_200_OK)
    


class MakeOrderFinished(APIView):

    def patch(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        order.status = 'finished'
        order.save()

        if order.active_type == 'price':
            global_points = GlobalPoints.get_instance()
            order.profile.points += order.total_price // global_points.purchase_points
            order.profile.save()
            if order.profile.referred_by is not None:
                refferal_profile = get_object_or_404(Profile, telegram_id=order.profile.referred_by)
                refferal_profile.points += order.total_price // global_points.referral_purchase_points
                refferal_profile.save()
        return Response({'success':'success'}, status=status.HTTP_200_OK)


class GetFinishedOrders(APIView):
    
    def get(self, request):
        orders = Order.objects.filter(status='finished')

        json_orders = []

        for order in orders:

            json_order = {}
            json_order['customer_info'] = order.customer_info
            json_order['تاريخ الطلب:'] = order.created_at.strftime('%Y-%m-%d %H:%M')
            json_order['تاريخ القبول:'] = order.purchased_at.strftime('%Y-%m-%d %H:%M')
            if order.active_type == "price":
                sells = []
                for order_item in order.orderitem_set.all():
                    sells.append(f"  - {order_item.quantity} × {order_item.item.name}")
                
                json_order["مشتريات العناصر :"] = sells.copy()
                
                sells.clear()
                
                for order_package in order.orderpackage_set.all():
                    sells.append(f"  - {order_package.quantity} × {order_package.package.name}")
                json_order[f"مشتريات البكجات :"] = sells.copy()

                json_order["السعر الكلي:"] =  order.total_price

            elif order.active_type == "point":
                sells = []
                for order_point_item in order.orderpointitem_set.all():
                    sells.append(f"  - {order_point_item.quantity} × {order_point_item.point_item.name}")
                
                json_order["المشتريات :"] = sells

                json_order["إجمالي النقاط:"] = order.total_points

            json_orders.append(json_order)
        
        return Response(json_orders, status=status.HTTP_200_OK)
