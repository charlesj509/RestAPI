from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .models import Products
from .serializers import ProductsSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':

        products = Products.objects.all()

        serializer = ProductsSerializer(products, many=True)


        return Response(serializer.data)