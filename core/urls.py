from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


def index(request):
    from django.shortcuts import render

    return render(request, "home.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("rosetta/", include("rosetta.urls")),
    path("", index),
    path("about/", include("about.urls")),
]

if settings.DEBUG:
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
    urlpatterns += [path("ckeditor5/", include("django_ckeditor_5.urls"))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
