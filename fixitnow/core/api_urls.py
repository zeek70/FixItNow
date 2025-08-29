from rest_framework.routers import DefaultRouter
from .api_views import (
    UserViewSet, CategoryViewSet,
    ServiceRequestViewSet, ServiceUpdateViewSet, AboutViewSet,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'service-requests', ServiceRequestViewSet)
router.register(r'service-updates', ServiceUpdateViewSet)
router.register(r'about', AboutViewSet)

urlpatterns = router.urls

