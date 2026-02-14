
from rest_framework.routers import DefaultRouter
from app.product.views import ProductViewSet, FavoriteVIewSet, CartViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")
router.register("favorites", FavoriteVIewSet, basename="favorites")
router.register("cart", CartViewSet, basename="cart")

urlpatterns = router.urls