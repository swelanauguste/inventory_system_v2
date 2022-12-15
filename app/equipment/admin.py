from django.contrib import admin

from .models import Group, Equipment, Manufacturer, Ink

admin.site.register(Group)
admin.site.register(Equipment)
admin.site.register(Manufacturer)
admin.site.register(Ink)