from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path

urlpatterns = [
                  re_path(r'^admin/', admin.site.urls),
                  path("", include('store.urls'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)