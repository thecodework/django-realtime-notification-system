from django.urls import re_path

from notification_app.consumers import NotificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/notification/(?P<room_name>\w+)/$', NotificationConsumer.as_asgi()),
]
