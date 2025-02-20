from rest_framework.generics import RetrieveAPIView
from item.models import Category, Item
from item.serializers import CategorySerializer, ItemSerializer

# Create your views here.

class AllItmes(RetrieveAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'


class GetItem(RetrieveAPIView):

    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_field = 'id'
