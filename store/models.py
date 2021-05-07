from django.db import models

# Create your models here.
from django_logic import ProcessManager

from .process import COOPERATION_PARTNER_STATE_REGISTERED, \
    CooperationPartnerProcess

LockProcess = ProcessManager.bind_state_fields(status=CooperationPartnerProcess)


class Lock(LockProcess, models.Model):
    status = models.CharField(
        choices=CooperationPartnerProcess.states,
        default=COOPERATION_PARTNER_STATE_REGISTERED,
        max_length=30, blank=True)
    customer_received_notice = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.status

