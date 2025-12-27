from django.contrib import admin
from .models import Place, PlaceImage
# Register your models here.

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    ordering = ('position',)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
    list_display = ('name', 'lat', 'lng')
    
@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'position')
    list_filter = ('place',)
    ordering = ('place', 'position')    