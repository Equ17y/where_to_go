from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = 'Load place from JSON URL'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='URL to JSON file')

    def handle(self, *args, **options):
        url = options['url']
        try:
            response = requests.get(url)
            response.raise_for_status()
            raw_place = response.json()
        except requests.RequestException as e:
            self.stderr.write(f'Error downloading JSON: {e}')
            return
        except ValueError as e:
            self.stderr.write(f'Invalid JSON: {e}')
            return

        place, created = Place.objects.update_or_create(
            name=raw_place['title'],
            defaults={
                'short_description': raw_place.get('description_short', ''),
                'long_description': raw_place.get('description_long', ''),
                'lat': raw_place['coordinates']['lat'],
                'lng': raw_place['coordinates']['lng'],
            },
        )
        
        action = "Updated" if not created else "Created"
        self.stdout.write(f"{action} place: {place.name}")

        for img_url in raw_place.get('imgs', []):
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()

                filename = urlparse(img_url).path.split('/')[-1] or 'image.jpg'

                image_obj, img_created = PlaceImage.objects.get_or_create(
                    place=place, image=f'places/{filename}'
                )

                if img_created:
                    image_obj.image.save(
                        filename, ContentFile(img_response.content), save=True
                    )
                    self.stdout.write(f'  Added image: {filename}')
                else:
                    self.stdout.write(f'  Image already exists: {filename}')

            except requests.RequestException as e:
                self.stderr.write(f'  Failed to download {img_url}: {e}')
            except Exception as e:
                self.stderr.write(f'  Error saving image: {e}')
