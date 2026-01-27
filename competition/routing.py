from django.urls import re_path

from .consumers import ChallengeConsumer, ChallengeLeaderboardConsumer, LeaderboardConsumer, SubmissionConsumer

websocket_urlpatterns = [
    re_path(r"^ws/challenges/stream/$", ChallengeConsumer.as_asgi()),
    re_path(r"^ws/submissions/$", SubmissionConsumer.as_asgi()),
    re_path(r"^ws/leaderboard/$", LeaderboardConsumer.as_asgi()),
    re_path(r"^ws/challenges/(?P<challenge_id>[^/]+)/$", ChallengeLeaderboardConsumer.as_asgi()),
]
