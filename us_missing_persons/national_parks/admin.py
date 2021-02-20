from django.contrib import admin
from .models import NationalParks

from import_export.admin import ImportExportModelAdmin
from import_export import resources


class NationalParksResource(resources.ModelResource):
    """Used for django-import-export library."""

    class Meta:
        model = NationalParks


@admin.register(NationalParks)
class NationalParksAdminModel(ImportExportModelAdmin):
    """Used for django-import-export library."""

    resource_class = NationalParksResource
    ordering = ("title",)
