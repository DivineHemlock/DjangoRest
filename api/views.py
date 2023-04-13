from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from api.serializers import ProductSerializer

from api.models import Product


@api_view(["GET"])
def api_home(request):
    model = Product.objects.all().order_by("?").first()
    data = model_to_dict(model)
    data = ProductSerializer(model).data
    return Response(data)
