from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/v1/', include([
      path('auth/', include('accounts.urls')),
      path('', include('sections.urls.new.urls_new')),
      path('', include('sections.urls.category.urls_category')),
      path('', include('sections.urls.stock.urls_stock')),
      path('', include('sections.urls.realty.urls_realty')),
      path('docs/', include([
          path('', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
          path('api.json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),
          path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
      ])),
  ]))
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
