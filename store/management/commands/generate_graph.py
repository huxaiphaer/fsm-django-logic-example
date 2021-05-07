from django.core.management import BaseCommand
from django_logic.display import display_process

from store.process import CooperationPartnerProcess, \
    COOPERATION_PARTNER_STATE_REGISTERED


class Command(BaseCommand):

    help = 'Generate graph.'

    def handle(self, *args, **kwargs):
        display_process(CooperationPartnerProcess,
                        state=COOPERATION_PARTNER_STATE_REGISTERED,
                        skip_main_process=True)
