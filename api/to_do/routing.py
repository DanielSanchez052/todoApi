from django.urls import path
from api.to_do.consumers import ToDoConsumer

websocket_urlpatterns=[
    path('ws/test/<str:name>/',ToDoConsumer.as_asgi(),name='test')
]


