from rest_framework.generics import RetrieveAPIView, ListAPIView
from item.models import Category, Item, Package
from item.serializers import ItemSerializer, PackageSerializer, PackageItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.

class AllItmes(APIView):

    def get(self, request, id, item_type):
        category = get_object_or_404(Category, id=id)

        filtered_items = category.items.filter(item_type=item_type).order_by('id')

        return Response(ItemSerializer(filtered_items, many=True).data, status=status.HTTP_200_OK)


class GetItem(RetrieveAPIView):

    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_field = 'id'


class GetPackages(ListAPIView):

    serializer_class = PackageSerializer
    queryset = Package.objects.all()


class GetPackagesItems(ListAPIView):
    serializer_class = PackageItemSerializer

    def get_queryset(self):
        package_id = self.kwargs.get('id')
        package = get_object_or_404(Package, id=package_id)
        return package.items.all()