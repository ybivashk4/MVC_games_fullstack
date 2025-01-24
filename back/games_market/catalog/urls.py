from rest_framework import routers
from catalog.views import CatalogViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register('catalog', viewset=CatalogViewSet)

urlpatterns = router.urls
