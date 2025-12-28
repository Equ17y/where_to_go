from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from tinymce.widgets import TinyMCE

from .models import Place, PlaceImage

# Register your models here.


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 1
    ordering = ("position",)
    readonly_fields = ("image_preview",)
    fields = ("image", "image_preview")

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; width: auto; '
                'border: 1px solid #ccc;"/>',
                obj.image.url,
            )
        return "Нет изображения"

    image_preview.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PlaceImageInline]
    list_display = ("name", "lat", "lng")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["description_long"].widget = TinyMCE()
        return form
