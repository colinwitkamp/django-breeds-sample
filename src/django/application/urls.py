from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path

admin.autodiscover()

# ------------------------------------------------------------ #

# ----------------------------------------------- #
# URL patterns
# ----------------------------------------------- #
app_name = "application"

# Application patterns.
urlpatterns = [
    # Third party URLs.
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("breeds/", include('breeds.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
