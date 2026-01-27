from channels.generic.websocket import AsyncJsonWebsocketConsumer


class LeaderboardConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("leaderboard", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("leaderboard", self.channel_name)

    async def leaderboard_update(self, event):
        await self.send_json(event["payload"])


class ChallengeLeaderboardConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.challenge_id = self.scope["url_route"]["kwargs"]["challenge_id"]
        self.group_name = f"challenge_{self.challenge_id}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def leaderboard_update(self, event):
        await self.send_json(event["payload"])


class SubmissionConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("submissions", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("submissions", self.channel_name)

    async def submission_update(self, event):
        await self.send_json(event["payload"])


class ChallengeConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("challenges", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("challenges", self.channel_name)

    async def challenge_update(self, event):
        await self.send_json(event["payload"])
