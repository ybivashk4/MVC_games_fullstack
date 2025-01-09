from rest_framework import routers
from descriptions.views import DescriptionViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register('description', viewset=DescriptionViewSet)

urlpatterns = router.urls
