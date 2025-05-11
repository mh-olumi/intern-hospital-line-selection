import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CapacityConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join a group to broadcast capacity updates
        await self.channel_layer.group_add(
            "capacity_updates",
            self.channel_name
        )
        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave the group on disconnect
        await self.channel_layer.group_discard(
            "capacity_updates",
            self.channel_name
        )
    
    # This handler is called when a message is sent to the group.
    async def capacity_update(self, event):
        capacity_data = event['data']
        await self.send(text_data=json.dumps({
            'data': capacity_data
        }))