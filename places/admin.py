from django.contrib import admin
from .models import Place, PlaceImage
# Register your models here.

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'position')
    list_filter = ('place',)
    ordering = ('place', 'position')    