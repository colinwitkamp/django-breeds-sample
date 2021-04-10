import requests
import os
import urllib.request

from django.conf import settings
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from breeds.models import Breed as Breed
from breeds.models import Style as BreedStyle
from breeds.models import Image as BreedImage


class Command(BaseCommand):
    help = "Fetch breeds from Dog API"

    def handle(self, *args, **options):

        # Clear table
        Breed.objects.all().delete()

        # Clear files
        dir_path = os.path.join(settings.MEDIA_ROOT, "breeds")

        try:
            os.mkdir(dir_path)
        except:
            pass
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        data = response.json()
        breeds = data.get("message")
        if breeds is not None:
            for (index, breed_name) in enumerate(breeds):
                # Make dir
                breed_path = dir_path + "/" + breed_name
                try:
                    os.mkdir(breed_path)
                except:
                    pass

                response = requests.get(
                    "https://dog.ceo/api/breed/%s/images" % breed_name
                )
                image_data = response.json()
                images = image_data.get("message")
                breed = Breed.objects.create(
                    name=breed_name, image_count=len(images), create_date=timezone.now()
                )

                styles = breeds.get(breed_name)
                breed_styles = []
                for style in styles:
                    breed_styles.append(BreedStyle(name=style, breed=breed))
                BreedStyle.objects.bulk_create(breed_styles)

                file_names = []
                if images is not None:
                    # create images
                    last_images = images[-20:]
                    for url in last_images:
                        file_name = url.rsplit("/", 1)[-1]

                        file_names.append(
                            BreedImage(
                                breed=breed, path=breed_name + "/" + file_name, url=url
                            )
                        )

                    image_objs = BreedImage.objects.bulk_create(file_names)
                    # save image files
                    for (img_index, img) in enumerate(image_objs):
                        urllib.request.urlretrieve(img.url, dir_path + "/" + img.path)
                        self.stdout.write(
                            self.style.SUCCESS(
                                "fetched img for %s - %d/%d."
                                % (breed_name, (img_index + 1), len(image_objs))
                            )
                        )

                    self.stdout.write(
                        self.style.SUCCESS(
                            "Breed %d/%d completed!" % (index + 1, len(breeds))
                        )
                    )

            self.stdout.write(self.style.SUCCESS("Successfully imported breeds!"))
        else:
            self.stdout.write(self.style.WARNING("Failed to fetch breeds"))
