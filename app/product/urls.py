from django.urls import path
from app.product.views import ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name='product-list'),
    path("products/<uuid:uuid>/", ProductDetailAPIView.as_view(), name='prodcut-detail')
]
