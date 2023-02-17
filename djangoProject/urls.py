from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

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

    #music app
    path('', include('music.urls')),

    #jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #swagger
    path('doc', schema_view.with_ui('swagger', cache_timeout=0), name='doc_swagg'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='doc_redoc')
]
