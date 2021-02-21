from django.db import models


class Core(models.Model):
    """ This is the Core of our app. """

    pass

    class Meta:
        verbose_name = "Core"
        verbose_name_plural = "Core"

    def __str__(self):
        return self.name
