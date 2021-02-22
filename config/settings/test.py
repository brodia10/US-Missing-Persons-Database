from .base import *


DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.spatialite",
        "NAME": "test.db",
    }
}

SPATIALITE_LIBRARY_PATH = "/usr/local/lib/mod_spatialite.dylib"
