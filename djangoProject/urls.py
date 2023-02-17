from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title='Music API',
        default_version='v1',
        description='Music api for test',
        contact=openapi.Contact(email='savridinovs123@gamil.com')
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('music.urls')),

    path('doc', schema_view.with_ui('swagger', cache_timeout=0), name='doc_swagg'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='doc_redoc')
]
