from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = "Load place from JSON URL"

    def add_arguments(self, parser):
        parser.add_argument("url", type=str, help="URL to JSON file")

    def handle(self, *args, **options):
        url = options["url"]
        try:
            response = requests.get(url)
            response.raise_for_status()
            place_data = response.json()
        except requests.RequestException as e:
            self.stderr.write(f"Error downloading JSON: {e}")
            return
        except ValueError as e:
            self.stderr.write(f"Invalid JSON: {e}")
            return

        place, created = Place.objects.get_or_create(
            name=place_data["title"],
            defaults={
                "short_description": place_data.get("short_description", ""),
                "long_description": place_data.get("long_description", ""),
                "lat": place_data["coordinates"]["lat"],
                "lng": place_data["coordinates"]["lng"],
            },
        )

        if not created:
            place.short_description = place_data.get("description_short", "")
            place.long_description = place_data.get("description_long", "")
            place.lat = place_data["coordinates"]["lat"]
            place.lng = place_data["coordinates"]["lng"]
            place.save()
            self.stdout.write(f"Updated place: {place.name}")
        else:
            self.stdout.write(f"Created place: {place.name}")

        for img_url in place_data.get("imgs", []):
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()

                filename = urlparse(img_url).path.split("/")[-1] or "image.jpg"

                image_obj, img_created = PlaceImage.objects.get_or_create(
                    place=place, image=f"places/{filename}"
                )

                if img_created:
                    image_obj.image.save(
                        filename, ContentFile(img_response.content), save=True
                    )
                    self.stdout.write(f"  Added image: {filename}")
                else:
                    self.stdout.write(f"  Image already exists: {filename}")

            except requests.RequestException as e:
                self.stderr.write(f"  Failed to download {img_url}: {e}")
            except Exception as e:
                self.stderr.write(f"  Error saving image: {e}")
