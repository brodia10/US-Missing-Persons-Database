from django.db import models


class NationalParks(models.Model):
    """
    This is the National Parks model.
    """

    id = models.UUIDField(primary_key=True)
    area_acres = models.FloatField()
    area_square_km = models.FloatField()
    coordinates_latitude = models.FloatField()
    coordinates_longitude = models.FloatField()
    date_established = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=500)
    image_url = models.CharField(max_length=50)
    image_attribution = models.CharField(max_length=150)
    image_attribution_url = models.CharField(max_length=150)
    nps_link = models.CharField(max_length=150)
    states_id = models.CharField(max_length=150)
    states_title = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    park_id = models.CharField(max_length=150)
    visitors = models.IntegerField()
    world_heritage_site = models.BooleanField(null=True, blank=True)

    class Meta:
        verbose_name = "National Parks"
        verbose_name_plural = "National Parkss"

    def __str__(self):
        return self.title
