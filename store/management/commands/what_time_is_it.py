from django.utils import timezone
from django.core.management import BaseCommand


class Command(BaseCommand):

    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)