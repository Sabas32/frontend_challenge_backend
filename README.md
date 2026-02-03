# Django Backend

## Setup

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py seed_challenges
python manage.py runserver
```

## Seed data (local)

- `seed_demo` creates demo users with Ugandan names.
- `seed_challenges` wipes and recreates challenges (25 total).

## API

- `GET /api/auth/csrf/` - set CSRF cookie
- `POST /api/auth/login/` - login with session cookie
- `POST /api/auth/register/` - register student competitor account (requires one-time invite code)
- `GET /api/auth/registration-codes/` - list latest invite codes (admin)
- `POST /api/auth/registration-codes/` - create invite code (admin, expires in 20 minutes)
- `DELETE /api/auth/registration-codes/<id>/` - revoke invite code (admin)
- `POST /api/auth/logout/` - logout
- `GET /api/auth/me/` - current user
- `GET /api/auth/system-status/` - current access state
- `PATCH /api/auth/system-status/` - admin toggle for competitor access
- `GET /api/auth/system-schedules/` - list schedules
- `POST /api/auth/system-schedules/` - create schedule (admin)
- `PATCH /api/auth/system-schedules/<id>/` - enable/disable/update (admin)
- `DELETE /api/auth/system-schedules/<id>/` - delete (admin)
- `GET /api/auth/users/` - list all users (admin)
- `GET /api/challenges/` - list challenges
- `POST /api/challenges/` - create (admin)
- `GET /api/submissions/` - list submissions (admin sees all)
- `POST /api/submissions/` - create (include `submission_type: final` to publish leaderboard entry)
- `GET /api/leaderboard/` - list leaderboard entries

## WebSockets

- `ws://localhost:8000/ws/leaderboard/`
- `ws://localhost:8000/ws/challenges/<challenge_id>/`
- `ws://localhost:8000/ws/submissions/`
- `ws://localhost:8000/ws/challenges/stream/`
- `ws://localhost:8000/ws/system-status/`


## Environment Flags

- ENABLE_INVITE_REGISTRATION=false (recommended in production unless needed).
- When disabled, /api/auth/register/ and /api/auth/registration-codes/* return 404.

