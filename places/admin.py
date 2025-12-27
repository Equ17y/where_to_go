from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import format_html
# Register your models here.

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    ordering = ('position',)
    readonly_fields = ('image_preview',)
    fields = ('image', 'image_preview', 'position')
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; width: auto; border: 1px solid #ccc;"/>',
                obj.image.url
            )
        return
    
    image_preview.short_description = "Превью"
    

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
    list_display = ('name', 'lat', 'lng')
    
@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'position')
    list_filter = ('place',)
    ordering = ('place', 'position')
    readonly_fields = ('image_preview',)
    fields = ('place', 'image', 'image_preview', 'position')
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; width: auto; border: 1px solid #ccc;"/>',
                obj.image.url
            )
        return
    
    image_preview.short_description = "Превью"    