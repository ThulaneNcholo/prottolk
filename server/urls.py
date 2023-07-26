from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from client.sitemaps import StaticViewsSitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    "sitemap": StaticViewsSitemap
}


# ERROR PAGE VIEWS
handler400 = 'server.views.handler400'
handler403 = 'server.views.handler403'
handler404 = 'server.views.handler404'
handler500 = 'server.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls', namespace="client")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    )
]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
