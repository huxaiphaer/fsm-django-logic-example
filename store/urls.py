from django.urls import path
from store.views import LockerAPIView

app_name = 'api'

urlpatterns = [
    path('locks/', LockerAPIView.as_view(), name='locks'),
]




