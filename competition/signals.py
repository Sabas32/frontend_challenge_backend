from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Challenge, LeaderboardEntry, Submission
from .serializers import ChallengeSerializer


@receiver(post_save, sender=LeaderboardEntry)
def broadcast_leaderboard_update(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    payload = {
        "type": "leaderboard.update",
        "action": "created" if created else "updated",
        "entry": {
            "id": str(instance.id),
            "challengeId": instance.challenge_id,
            "challengeTitle": instance.challenge.title,
            "userId": instance.user_id,
            "username": instance.user.username,
            "name": instance.user.get_full_name() or instance.user.username,
            "school": getattr(instance.user, "school", ""),
            "score": instance.score_total,
            "breakdown": instance.score_breakdown or {},
            "timestamp": instance.created_at.isoformat(),
        },
    }
    async_to_sync(channel_layer.group_send)(
        "leaderboard", {"type": "leaderboard_update", "payload": payload}
    )
    async_to_sync(channel_layer.group_send)(
        f"challenge_{instance.challenge_id}",
        {"type": "leaderboard_update", "payload": payload},
    )


@receiver(post_delete, sender=LeaderboardEntry)
def broadcast_leaderboard_delete(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    payload = {
        "type": "leaderboard.delete",
        "action": "deleted",
        "entry": {
            "id": str(instance.id),
            "challengeId": instance.challenge_id,
            "userId": instance.user_id,
        },
    }
    async_to_sync(channel_layer.group_send)(
        "leaderboard", {"type": "leaderboard_update", "payload": payload}
    )
    async_to_sync(channel_layer.group_send)(
        f"challenge_{instance.challenge_id}",
        {"type": "leaderboard_update", "payload": payload},
    )


@receiver(post_delete, sender=Submission)
def broadcast_submission_delete(sender, instance, **kwargs):
    if instance.submission_type != "final":
        return
    channel_layer = get_channel_layer()
    payload = {
        "type": "submission.reopen",
        "action": "deleted",
        "submission": {
            "id": str(instance.id),
            "challengeId": instance.challenge_id,
            "userId": instance.user_id,
            "username": instance.user.username,
            "submissionType": instance.submission_type,
        },
    }
    async_to_sync(channel_layer.group_send)(
        "submissions", {"type": "submission_update", "payload": payload}
    )


@receiver(post_save, sender=Submission)
def broadcast_submission_create(sender, instance, created, **kwargs):
    if instance.submission_type != "final":
        return
    channel_layer = get_channel_layer()
    payload = {
        "type": "submission.created" if created else "submission.updated",
        "action": "created" if created else "updated",
        "submission": {
            "id": str(instance.id),
            "challengeId": instance.challenge_id,
            "userId": instance.user_id,
            "username": instance.user.username,
            "name": instance.user.get_full_name() or instance.user.username,
            "school": getattr(instance.user, "school", ""),
            "submissionType": instance.submission_type,
            "timestamp": instance.created_at.isoformat(),
        },
    }
    async_to_sync(channel_layer.group_send)(
        "submissions", {"type": "submission_update", "payload": payload}
    )


@receiver(post_save, sender=Challenge)
def broadcast_challenge_create(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    payload = {
        "type": "challenge.created" if created else "challenge.updated",
        "action": "created" if created else "updated",
        "challenge": ChallengeSerializer(instance).data,
    }
    async_to_sync(channel_layer.group_send)(
        "challenges", {"type": "challenge_update", "payload": payload}
    )


@receiver(post_delete, sender=Challenge)
def broadcast_challenge_delete(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    payload = {
        "type": "challenge.deleted",
        "action": "deleted",
        "challenge": {
            "id": instance.id,
        },
    }
    async_to_sync(channel_layer.group_send)(
        "challenges", {"type": "challenge_update", "payload": payload}
    )
