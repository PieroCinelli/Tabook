from django.urls import re_path
from .consumers import ReservationConsumer

websocket_urlpatterns = [
    re_path(r'ws/reservations/$', ReservationConsumer.as_asgi()),
]
