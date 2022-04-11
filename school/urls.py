from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from .sitemaps import CourseSitemap, StaticViewSitemap, EventSitemap


sitemaps = {
    'education': CourseSitemap,
    'events': EventSitemap,
    'static': StaticViewSitemap,
    }


urlpatterns = [
    path('api/', include('mainapp.api.urls')),
    path('api/admin/', admin.site.urls),
    path('api/crm/', include('management.urls')),
    path('api/management/', include('management.api.urls')),
    path('api/api-auth/', include('rest_framework.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
