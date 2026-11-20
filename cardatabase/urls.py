from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  
    TokenRefreshView,
)

from cars.views import CarViewSet, OwnerViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'owners', OwnerViewSet, basename='owner')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(
        'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'swagger-ui.html',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
]