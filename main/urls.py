from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import ArticleViewSet, OrderViewSet


router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
