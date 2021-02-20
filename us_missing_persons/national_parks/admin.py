from .models import NationalParks

from import_export.admin import ImportExportModelAdmin
from import_export import resources

from django.contrib import admin


class NationalParksResource(resources.ModelResource):
    """Used for django-import-export library."""

    class Meta:
        model = NationalParks


class NationalParksAdminModel(ImportExportModelAdmin):
    """Used for django-import-export library."""

    resource_class = NationalParksResource

    ordering = ("title",)

    list_display = [
        "title",
        "states_title",
        "short_description",
        "date_established",
        "visitors",
        "nps_link",
        "image_url",
        "image_attribution",
        "image_attribution_url",
        "world_heritage_site",
        "area_acres",
        "area_square_km",
        "coordinates_latitude",
        "coordinates_longitude",
    ]

    list_filter = ["title", "states_title", "world_heritage_site"]

    search_fields = ["title", "states_title"]


admin.site.register(NationalParks, NationalParksAdminModel)
