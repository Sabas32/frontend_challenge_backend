from django.utils import timezone

from .models import SystemSchedule
from .serializers import SystemScheduleSerializer


def get_schedule_context(now=None):
    if now is None:
        now = timezone.now()
    enabled = SystemSchedule.objects.filter(enabled=True)
    active = (
        enabled.filter(close_at__lte=now, open_at__gt=now)
        .order_by("open_at")
        .first()
    )
    upcoming = (
        enabled.filter(close_at__gt=now)
        .order_by("close_at")
        .first()
    )
    return active, upcoming


def apply_schedule_state(state):
    now = timezone.now()
    active, upcoming = get_schedule_context(now=now)
    changed = False
    paused_now = False
    resumed_now = False

    if active:
        if state.allow_competitor_access or not state.scheduled_pause_active:
            state.allow_competitor_access = False
            state.scheduled_pause_active = True
            state.save(
                update_fields=[
                    "allow_competitor_access",
                    "scheduled_pause_active",
                    "updated_at",
                ]
            )
            changed = True
            paused_now = True
    else:
        if state.scheduled_pause_active:
            state.allow_competitor_access = True
            state.scheduled_pause_active = False
            state.save(
                update_fields=[
                    "allow_competitor_access",
                    "scheduled_pause_active",
                    "updated_at",
                ]
            )
            changed = True
            resumed_now = True

    return {
        "active": active,
        "upcoming": upcoming,
        "changed": changed,
        "paused_now": paused_now,
        "resumed_now": resumed_now,
    }


def build_system_status_payload(state, schedule_context=None):
    if schedule_context is None:
        active, upcoming = get_schedule_context()
        schedule_context = {"active": active, "upcoming": upcoming}
    active = schedule_context.get("active")
    upcoming = schedule_context.get("upcoming")
    pause_until = upcoming.close_at if upcoming else None
    resume_at = active.open_at if active else None
    schedules = SystemScheduleSerializer(
        SystemSchedule.objects.all(), many=True
    ).data
    return {
        "allow_competitor_access": state.allow_competitor_access,
        "scheduled_pause_active": state.scheduled_pause_active,
        "updated_at": state.updated_at,
        "pause_until": pause_until,
        "resume_at": resume_at,
        "schedules": schedules,
    }
