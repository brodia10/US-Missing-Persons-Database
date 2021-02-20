from django.db import models
from django.template.defaultfilters import truncatechars


class NationalParks(models.Model):
    """
    This is the National Parks model.
    """

    id = models.CharField(max_length=50, primary_key=True)
    area_acres = models.CharField(null=True, blank=True, max_length=50)
    area_square_km = models.CharField(null=True, blank=True, max_length=50)
    coordinates_latitude = models.CharField(null=True, blank=True, max_length=50)
    coordinates_longitude = models.CharField(null=True, blank=True, max_length=50)
    date_established = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image_url = models.CharField(max_length=50)
    image_attribution = models.CharField(max_length=150)
    image_attribution_url = models.CharField(max_length=150)
    nps_link = models.CharField(max_length=150)
    states_title = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    visitors = models.CharField(max_length=50)
    world_heritage_site = models.BooleanField(default=True)

    class Meta:
        verbose_name = "National Parks"
        verbose_name_plural = "National Parks"

    def __str__(self):
        """ Returns the string representation of National Parks. """
        return f"{self.title} National Park"

    @property
    def short_description(self):
        """ Truncates the description field to the specified length. """
        return truncatechars(self.description, 100)
