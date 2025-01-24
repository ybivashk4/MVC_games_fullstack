from rest_framework import routers
from .views import WishListViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register('wishlist', viewset=WishListViewSet)

urlpatterns = router.urls
