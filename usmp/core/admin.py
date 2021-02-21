from django.contrib import admin
from django.contrib.gis import admin as gis
from .models import WorldBorder


admin.site.register(WorldBorder, gis.OSMGeoAdmin)
