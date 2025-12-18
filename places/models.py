from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.CharField(max_length=300, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name