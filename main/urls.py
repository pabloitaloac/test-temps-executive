from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import ArticleViewSet, OrderViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Article and Order Management API",
      default_version='v1',
      description="API for managing articles and orders, including CRUD operations for both.",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]
