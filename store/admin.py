from django.contrib import admin

# Register your models here.
from store.models import Lock


@admin.register(Lock)
class LockerAdmin(admin.ModelAdmin):
    pass
