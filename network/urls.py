from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from network.views import SupplierViewSet, NetworkNodeViewSet

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'network-nodes', NetworkNodeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
