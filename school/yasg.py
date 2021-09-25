from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

description = "Разработчик - <b style='font-size: 20px;'>Голов Дмитрий Евгеньевич</b>\n" \
              "\n<b style='font-size: 20px;'>Контакты для связи:</b>" \
              "\nТелефон: +7 (902) 300-11-12, " \
              "\nemail: dgolov@icloud.com" \
              "\ntelegram: @dmgolov"

schema_view = get_schema_view(
   openapi.Info(
      title="Документация к API Академии Будущего",
      default_version='v1',
      description=description,
      license=openapi.License(name="Academy of Future License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
