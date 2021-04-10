from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize

from breeds.models import Breed as Breed
from breeds.models import Style as BreedStyle
from breeds.models import Image as BreedImage

# Create your views here.


def index(request):
    breeds = Breed.objects.select_related().all()
    results = []
    for breed in breeds:
        styles = BreedStyle.objects.filter(breed=breed)

        results.append({
          'name': breed.name,
          'styles': list(map(lambda s: s.name, styles))
        })
        
    data = serialize("json", breeds, fields=("name", "image_count"))
    return JsonResponse(results, safe=False)
