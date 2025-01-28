from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from orders.views import OrdersViewSet
from products.views import ProductsViewSet
from user.views import UserViewSet


router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("products", ProductsViewSet)
router.register("orders", OrdersViewSet)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Hubbi API",
        description="Marketplace de peças",
        default_version = "v1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
        ),
        
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path(
        "swagger/", 
        schema_view.with_ui("swagger", cache_timeout=0), 
        name="schema-swagger-ui"
    ), 
]
