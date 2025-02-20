from rest_framework.generics import RetrieveAPIView
from item.models import Category
from item.serializers import CategorySerializer

# Create your views here.

class AllItmes(RetrieveAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'
