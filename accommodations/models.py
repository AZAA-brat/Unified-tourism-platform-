from django.db import models

class Region(models.Model):
    name = models.CharField("Name of the Region", max_length=100)

    class Meta:
        verbose_name = "Regions"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name

