from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.product.models import Product
from app.product.serializers import ProductSerializer

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all().order_by("-created_at")
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
