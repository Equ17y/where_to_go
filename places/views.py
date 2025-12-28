from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from places.models import Place


def index(request):
    places = Place.objects.prefetch_related("images").all()
    features = []
    for place in places:
        if place.lng and place.lat:
            features.append(
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.lng, place.lat],
                    },
                    "properties": {
                        "title": place.name,
                        "placeId": place.id,
                        "detailsUrl": f"/places/{place.id}/",
                    },
                }
            )

    geojson = {"type": "FeatureCollection", "features": features}
    return render(request, "index.html", {"geojson_data": geojson})


def place_detail(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related("images"),
        id=place_id)

    response_data = {
        "title": place.name,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {"lng": place.lng, "lat": place.lat},
    }

    return JsonResponse(response_data, json_dumps_params={
                        "ensure_ascii": False})
