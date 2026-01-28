from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache

from app.product.models import Product
from app.product.serializers import ProductSerializer, ProductDetailSerializer

class ProductListAPIView(APIView):
    def get(self, request):
        cache_key = "product_list"
        cached_data = cache.get(cache_key)

        if cached_data:
            # print("\n\n\n\nCache\n\n\n\n")
            return Response(cached_data, status=status.HTTP_200_OK)

        # print("\n\n\n\nDB\n\n\n\n")

        products = (
            Product.objects
            .select_related("category", "model")
            .prefetch_related("images")
            .order_by("-created_at")
        )
        serializer = ProductSerializer(products, many=True)
        cache.set(cache_key, serializer.data, timeout=60 * 2)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailAPIView(APIView):
    def get(self, request, uuid):
        try:
            product = (Product.objects.select_related("category", "model")
            .prefetch_related("images").get(uuid=uuid))
        except Product.DoesNotExist:
            return Response({"error" : "Not Fount"}, status=404)

        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)