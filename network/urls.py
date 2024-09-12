from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from network.views import SupplierViewSet, NetworkNodeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'network-nodes', NetworkNodeViewSet)

urlpatterns = [
 path('admin/', admin.site.urls),
 path('api/', include(router.urls)),
 path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
 path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 path('api/auth/', include('djoser.urls')), # для регистрации и других функций
 path('api/auth/', include('djoser.urls.authtoken')), # для аутентификации через токен
]

