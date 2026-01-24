from django.urls import path
from app.product.views import ProductListAPIView

urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name='product-list')
]
