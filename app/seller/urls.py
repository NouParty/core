from rest_framework.routers import DefaultRouter

from .api import SellerViewSet

router = DefaultRouter()

router.register("all", SellerViewSet, basename="user")

urlpatterns = router.urls
