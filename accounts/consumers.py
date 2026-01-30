from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .models import SystemState
from django.contrib.sessions.models import Session
from .services import apply_schedule_state, build_system_status_payload
from django.utils import timezone
from .serializers import UserSerializer


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
        schedule_context = apply_schedule_state(state)
        return build_system_status_payload(state, schedule_context)


class OnlineUsersConsumer(AsyncJsonWebsocketConsumer):
    GROUP_NAME = "online_users"

    async def connect(self):
        user = self.scope.get("user")
        if not user or not user.is_authenticated or getattr(user, "role", None) != "admin":
            await self.close()
            return
        await self.channel_layer.group_add(self.GROUP_NAME, self.channel_name)
        await self.accept()
        users = await self._get_online_users()
        await self.send_json({"type": "online.users", "users": users})

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.GROUP_NAME, self.channel_name)

    async def online_users_update(self, event):
        await self.send_json({"type": "online.users", "users": event["payload"]})

    @database_sync_to_async
    def _get_online_users(self):
        active_sessions = Session.objects.filter(expire_date__gt=timezone.now())
        user_ids = set()
        for session in active_sessions:
            data = session.get_decoded()
            user_id = data.get("_auth_user_id")
            if user_id:
                user_ids.add(user_id)
        users = User.objects.filter(pk__in=user_ids).order_by("username")
        return UserSerializer(users, many=True).data
