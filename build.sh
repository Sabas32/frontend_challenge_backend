#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Optional: seed demo data on deploy (idempotent).
# Set SEED_DEMO=true in Render env vars, deploy once, then turn it off.
if [ "${SEED_DEMO:-false}" = "true" ]; then
  python manage.py seed_demo
  python manage.py seed_challenges
fi
