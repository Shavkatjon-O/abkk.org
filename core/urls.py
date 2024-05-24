from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import set_language
from django.conf import settings

from common.views import home_page_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("rosetta/", include("rosetta.urls")),
    path("", home_page_view),
    path("about/", include("about.urls")),
    path("set_language/", set_language, name="set_language"),
]

if settings.DEBUG:
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
