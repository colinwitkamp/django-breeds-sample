import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.serializers import serialize
from django.conf import settings
from breeds.models import Breed as Breed
from breeds.models import Style as BreedStyle
from breeds.models import Image as BreedImage

# Create your views here.


def index(request):
    breeds = Breed.objects.select_related().all()
    results = []
    for breed in breeds:
        styles = BreedStyle.objects.filter(breed=breed)

        results.append(
            {
                "name": breed.name,
                "image_count": breed.image_count,
                "styles": list(map(lambda s: s.name, styles)),
            }
        )

    return JsonResponse(results, safe=False)


def detail(request, breed_name):
    try:
        breed = Breed.objects.get(name=breed_name)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "breed_not_found"}, status=400)

    breed_styles = BreedStyle.objects.filter(breed=breed)
    breed_images = BreedImage.objects.filter(breed=breed)
    result = {
        "name": breed.name,
        "image_count": breed.image_count,
        "styles": list(map(lambda s: s.name, breed_styles)),
        "images": list(map(lambda i: settings.MEDIA_URL + "breeds/" + i.path, breed_images)),
    }

    return JsonResponse(result)
