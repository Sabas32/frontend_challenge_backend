from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Seed demo accounts for local development."

    def handle(self, *args, **options):
        User = get_user_model()
        users = [
            {
                "username": "admin",
                "password": "admin123",
                "role": "admin",
                "first_name": "Admin",
                "last_name": "Lead",
                "school": "Admin Office",
                "is_staff": True,
                "is_superuser": True,
            },
            {
                "username": "competitor",
                "password": "play123",
                "role": "competitor",
                "first_name": "Competitor",
                "last_name": "One",
                "school": "Frontier Tech Institute",
            },
            {
                "username": "ui-tester",
                "password": "ui2024",
                "role": "competitor",
                "first_name": "UI",
                "last_name": "Tester",
                "school": "Metro Design Academy",
            },
            {
                "username": "student",
                "password": "student123",
                "role": "competitor",
                "first_name": "Student",
                "last_name": "User",
                "school": "Riverside Tech College",
            },
        ]

        for payload in users:
            username = payload.pop("username")
            password = payload.pop("password")
            user, created = User.objects.get_or_create(username=username, defaults=payload)
            if created:
                user.set_password(password)
                user.save(update_fields=["password"])
                self.stdout.write(self.style.SUCCESS(f"Created {username}"))
            else:
                self.stdout.write(self.style.WARNING(f"Skipped {username} (already exists)"))
