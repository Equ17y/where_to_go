from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from where_to_go.views import index, place_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('places/<int:place_id>/', place_detail, name='place_detail'),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
