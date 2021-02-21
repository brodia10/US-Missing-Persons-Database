from django.contrib.gis.db import models
from pathlib import Path
from django.contrib.gis.utils import LayerMapping


class WorldBorder(models.Model):
    fips = models.CharField(max_length=2, null=True, blank=True)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.BigIntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


worldborder_mapping = {
    "fips": "FIPS",
    "iso2": "ISO2",
    "iso3": "ISO3",
    "un": "UN",
    "name": "NAME",
    "area": "AREA",
    "pop2005": "POP2005",
    "region": "REGION",
    "subregion": "SUBREGION",
    "lon": "LON",
    "lat": "LAT",
    "geom": "MULTIPOLYGON",
}

world_shp = Path(__file__).resolve().parent / ".." / "data" / "TM_WORLD_BORDERS-0.3.shp"


def load(verbose=True):
    lm = LayerMapping(WorldBorder, str(world_shp), worldborder_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
