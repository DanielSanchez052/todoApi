import json 
from channels.generic.websocket import JsonWebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from django.dispatch import receiver
from django.db.models.signals import post_save
from api.to_do.models import Task


class ToDoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['name']
        await self.channel_layer.group_add('test',self.channel_name)
        print("Connected...")
        self.accept()

    async def disconnect(self,code):
        await self.channel_layer.group_discard('test',self.channel_name)
        super().disconnect(code)
   
    async def send_update_task(self,event):
        await self.send_json({
            "message":"testMessage"
        })

