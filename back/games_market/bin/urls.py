from rest_framework import routers
from .views import BinViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register('wishlist', viewset=BinViewSet)

urlpatterns = router.urls
