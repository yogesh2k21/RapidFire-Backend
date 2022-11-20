from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep
from .models import Group, Chat
import asyncio
import json
from asgiref.sync import async_to_sync  # used in sync version to make async to sync
from channels.db import database_sync_to_async


class CustomSyncConsumer(WebsocketConsumer):
    def connect(self):
        print("web socket connected....")
        print("channel_name " + self.channel_name)
        print("channel_layer ", self.channel_layer)
        self.group_name = self.scope["url_route"]["kwargs"]["group_name"]
        # print('group_name '+self.scope['url_route']['kwargs']['group_name'])
        print("group_name ", self.group_name)
        # adding this channel to this given group_name which is come within the url as parameter
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("Message received from client...", text_data)
        data = json.loads(text_data)
        print(data)
        message = data["msg"]
        # print(message,'..................................')
        # group=Group.objects.get(name=self.group_name)
        # chat=Chat(content=message,group=group)
        # chat.save()
        # response={
        #     'type':'chat.message',
        #     'message':message
        # }
        # async_to_sync(self.channel_layer.group_send)(self.group_name,response)
        if self.scope["user"].is_authenticated:
            group = Group.objects.get(name=self.group_name)
            chat = Chat(content=message, group=group)
            chat.save()
            response = {"type": "chat.message", "message": message}
            async_to_sync(self.channel_layer.group_send)(self.group_name, response)
        else:
            self.send(text_data=json.dumps({"msg": "Login Required"}))
        # for i in range(10):
        #     self.send(text_data=f'Dataframe {i}')
        #     sleep(1)

    def chat_message(self, event):
        print("Event..", event)
        self.send(text_data=json.dumps({"msg": event["message"]}))

    def disconnect(self, code):
        print("web socket disconnected ", code)
        print("channel_name " + self.channel_name)
        print("channel_layer ", self.channel_layer)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )


class CustomAsyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("web socket connected....")
        print("channel_name " + self.channel_name)
        print("channel_layer ", self.channel_layer)
        self.group_name = self.scope["url_route"]["kwargs"]["group_name"]
        # print('group_name '+self.scope['url_route']['kwargs']['group_name'])
        print("group_name ", self.group_name)
        # adding this channel to this given group_name which is come within the url as parameter
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print("Message received from client...", text_data)
        data = json.loads(text_data)
        print(data)
        message = data["msg"]
        # group=await database_sync_to_async(Group.objects.get)(name=self.group_name)
        # chat=Chat(content=message,group=group)
        # await database_sync_to_async(chat.save)()
        # response={
        #     'type':'chat.message',
        #     'message':message
        # }
        # await self.channel_layer.group_send(self.group_name,response)
        if self.scope["user"].is_authenticated:
            group = await database_sync_to_async(Group.objects.get)(
                name=self.group_name
            )
            chat = Chat(content=message, group=group)
            await database_sync_to_async(chat.save)()
            response = {"type": "chat.message", "message": message}
            await self.channel_layer.group_send(self.group_name, response)
        else:
            await self.send(text_data=json.dumps({"msg": "Login Required"}))

    async def chat_message(self, event):
        print("Event..", event)
        await self.send(text_data=json.dumps({"msg": event["message"]}))

    async def disconnect(self, code):
        print("web socket disconnected ", code)
        print("channel_name " + self.channel_name)
        print("channel_layer ", self.channel_layer)
        await self.channel_layer.group_discard(self.group_name, self.channel_name)


"""
class MySyncConsumer(SyncConsumer):

    # this handler is called when client initially open a connection
    def websocket_connect(self, event):
        print("web socket connected....", event)
        self.send({'type': 'websocket.accept'})

    # when data received from client
    def websocket_receive(self, event):
        print("Message received from client...", event['text'])
        print(event['text'])
        for i in range(10):
            self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            sleep(1)

    # when connection is closed
    def websocket_disconnect(self, event):
        print("web socket disconnected", event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    # this handler is called when client initially open a connection
    async def websocket_connect(self, event):
        print("web socket connected....", event)
        await self.send({'type': 'websocket.accept'})

    # when data received from client
    async def websocket_receive(self, event):
        print("Message received from client...", event['text'])
        print(event['text'])
        for i in range(10):
            await self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            await asyncio.sleep(1)

    # when connection is closed
    async def websocket_disconnect(self, event):
        print("web socket disconnected", event)
        raise StopConsumer()
"""
