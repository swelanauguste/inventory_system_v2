from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("equipment.urls", namespace='equip')),
    path("admin/", admin.site.urls),
]
