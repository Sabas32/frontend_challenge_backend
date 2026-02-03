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
                "first_name": "Amina",
                "last_name": "Nabirye",
                "school": "Makerere Hill School",
            },
            {
                "username": "ui-tester",
                "password": "ui2024",
                "role": "competitor",
                "first_name": "Ronald",
                "last_name": "Ssemanda",
                "school": "Ndejje Senior School",
            },
            {
                "username": "student",
                "password": "student123",
                "role": "competitor",
                "first_name": "Sharon",
                "last_name": "Nakku",
                "school": "Gayaza High School",
            },
            {
                "username": "champion",
                "password": "champion123",
                "role": "competitor",
                "first_name": "Ivan",
                "last_name": "Kato",
                "school": "St. Mary's College Kisubi",
            },
            {
                "username": "builder",
                "password": "builder123",
                "role": "competitor",
                "first_name": "Dennis",
                "last_name": "Ssemwogerere",
                "school": "Buddo Secondary School",
            },
            {
                "username": "visuals",
                "password": "visuals123",
                "role": "competitor",
                "first_name": "Prisca",
                "last_name": "Nanyonga",
                "school": "Bweranyangi Girls",
            },
            {
                "username": "rookie",
                "password": "rookie123",
                "role": "competitor",
                "first_name": "Brian",
                "last_name": "Okello",
                "school": "Lubiri Secondary School",
            },
            {
                "username": "mentor",
                "password": "mentor123",
                "role": "viewer",
                "first_name": "Florence",
                "last_name": "Namatovu",
                "school": "ISCC Guests",
            },
            {
                "username": "judge",
                "password": "judge123",
                "role": "viewer",
                "first_name": "Richard",
                "last_name": "Sekandi",
                "school": "ISCC Panel",
            },
            {
                "username": "viewer",
                "password": "viewer123",
                "role": "viewer",
                "first_name": "Patricia",
                "last_name": "Achieng",
                "school": "Guest",
            },
            {
                "username": "mukono-star",
                "password": "mukono123",
                "role": "competitor",
                "first_name": "Joel",
                "last_name": "Muwonge",
                "school": "Mt. St. Henry's High School Mukono",
            },
            {
                "username": "namilyango-dev",
                "password": "namilyango123",
                "role": "competitor",
                "first_name": "Paul",
                "last_name": "Semakula",
                "school": "Namilyango College",
            },
            {
                "username": "namagunga-ui",
                "password": "namagunga123",
                "role": "competitor",
                "first_name": "Doreen",
                "last_name": "Nansubuga",
                "school": "Mt. St. Mary's College Namagunga",
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
