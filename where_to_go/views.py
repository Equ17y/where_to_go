import json
from pathlib import Path
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from places.models import Place

PLACE_JSON_MAP = {
    1: 'moscow_legends.json',
    2: 'roofs24.json',
}

def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        if place.lng and place.lat:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.name,
                    "placeId": place.id,
                    "detailsUrl": f"/places/{place.id}/"
                }
            })
    
    geojson = {"type": "FeatureCollection", "features": features}
    return render(request, "index.html", {"geojson_data": geojson})


def place_detail(request, place_id):
    get_object_or_404(Place, id=place_id)
    
    filename = PLACE_JSON_MAP.get(place_id)
    if not filename:
        return JsonResponse({'error': 'Not found'}, status=404)
    
    json_path = settings.BASE_DIR / 'static' / 'places' / filename
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    except FileNotFoundError:
        return JsonResponse({'error': 'JSON not found'}, status=404)