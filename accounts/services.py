from django.utils import timezone

from .models import SystemSchedule
from .serializers import SystemScheduleSerializer


def get_schedule_context(now=None):
    if now is None:
        now = timezone.now()
    enabled = SystemSchedule.objects.filter(enabled=True)
    active = (
        enabled.filter(open_at__lte=now, close_at__gt=now)
        .order_by("close_at")
        .first()
    )
    upcoming = (
        enabled.filter(open_at__gt=now)
        .order_by("open_at")
        .first()
    )
    completed_exists = enabled.filter(close_at__lte=now).exists()
    return active, upcoming, enabled.exists(), completed_exists


def apply_schedule_state(state):
    now = timezone.now()
    active, upcoming, has_enabled, completed_exists = get_schedule_context(
        now=now
    )
    changed = False
    paused_now = False
    resumed_now = False

    if has_enabled:
        should_allow = active is not None
        should_pause = not should_allow
        if (
            state.allow_competitor_access != should_allow
            or state.scheduled_pause_active != should_pause
        ):
            state.allow_competitor_access = should_allow
            state.scheduled_pause_active = should_pause
            state.save(
                update_fields=[
                    "allow_competitor_access",
                    "scheduled_pause_active",
                    "updated_at",
                ]
            )
            changed = True
            if should_pause:
                paused_now = True
            else:
                resumed_now = True
    else:
        if state.scheduled_pause_active:
            state.scheduled_pause_active = False
            state.save(update_fields=["scheduled_pause_active", "updated_at"])
            changed = True
    if completed_exists:
        SystemSchedule.objects.filter(close_at__lte=now).delete()

    return {
        "active": active,
        "upcoming": upcoming,
        "has_enabled": has_enabled,
        "completed_exists": completed_exists,
        "changed": changed,
        "paused_now": paused_now,
        "resumed_now": resumed_now,
    }


def build_system_status_payload(state, schedule_context=None):
    if schedule_context is None:
        active, upcoming, has_enabled, completed_exists = get_schedule_context()
        schedule_context = {
            "active": active,
            "upcoming": upcoming,
            "has_enabled": has_enabled,
            "completed_exists": completed_exists,
        }
    active = schedule_context.get("active")
    upcoming = schedule_context.get("upcoming")
    pause_until = active.close_at if active else None
    resume_at = upcoming.open_at if upcoming else None
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
