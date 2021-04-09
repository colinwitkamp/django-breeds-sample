from django.core.management.base import BaseCommand, CommandError
from breeds.models import Breed as Breed
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch breeds from Dog API'

    def handle(self, *args, **options):
        breed = Breed.objects.create(name="Joe", create_date=datetime.now())
  
        self.stdout.write(self.style.SUCCESS('Successfully created breed "%s"' % breed.name))
