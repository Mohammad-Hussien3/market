from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from item.models import Category, Item, Package, Order, PointItem, OrderItem, OrderPointItem, OrderPackage, GlobalPoints
from item.serializers import ItemSerializer, PackageSerializer, NewCategorySerializer, CategorySerializer, OrderSerializer, PointItemSerializer, GlobalPointsSerializer
from rest_framework.views import Response, status
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import json
from usermanagament.models import Profile

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


class DeleteItem(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
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


class UpdateCategory(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = NewCategorySerializer
    lookup_field = 'id'


class UpdatePackage(UpdateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    lookup_field = 'id'


class GetOrders(APIView):

    def get(self, request, telegram_id, status):
        orders = Order.objects.filter(profile__telegram_id=telegram_id, status=status)
        jsonOrders = OrderSerializer(orders, many=True).data
        return Response(jsonOrders)


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

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
    

class UpdateGlobalPointsView(APIView):
    def patch(self, request):
        instance = GlobalPoints.get_instance()
        serializer = GlobalPointsSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)