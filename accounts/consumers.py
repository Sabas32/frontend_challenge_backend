from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .models import SystemState


class SystemStatusConsumer(AsyncJsonWebsocketConsumer):
    GROUP_NAME = "system_status"

    async def connect(self):
        await self.channel_layer.group_add(self.GROUP_NAME, self.channel_name)
        await self.accept()
        state = await self._get_state()
        if state:
            await self.send_json(state)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.GROUP_NAME, self.channel_name)

    async def system_status_update(self, event):
        await self.send_json(event["payload"])

    @database_sync_to_async
    def _get_state(self):
        state = SystemState.current()
        if not state:
            return {"allow_competitor_access": True}
        return {
            "allow_competitor_access": state.allow_competitor_access,
        }
