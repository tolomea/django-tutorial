from django.urls import include, path
from django.contrib import admin
import debug_toolbar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
]
