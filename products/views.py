from rest_framework import generics
from api.models import Product
from api.serializers import ProductSerializer


class ProductDetailAPIview(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'title'
