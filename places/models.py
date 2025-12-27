from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField()
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")

    def __str__(self):
        return self.name
    
class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )
     
    image = models.ImageField(
        upload_to='places',
        verbose_name='Картинка'
    )
     
    position = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок'
    )
     
    class Meta:
       ordering = ['position']
        
    def __str__(self):
        return f'{self.place.name} ({self.position})'
        