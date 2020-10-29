import os

from allauth.socialaccount.models import SocialApp
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management import execute_from_command_line
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from users.models import User


class Command(BaseCommand):
    help = "Seed database. If you want facebook social auth set, remember about .env file."

    def add_arguments(self, parser):
        parser.add_argument(
            "--facebook-key",
            nargs="?",
            type=str,
            default=os.environ.get("SOCIAL_AUTH_FACEBOOK_KEY"),
        )
        parser.add_argument(
            "--facebook-secret",
            nargs="?",
            type=str,
            default=os.environ.get("SOCIAL_AUTH_FACEBOOK_SECRET"),
        )
        parser.add_argument(
            "--admin",
            action="store_true",
            help="Create superuser with random password (will be shown in the console)",
        )
        parser.add_argument(
            "--reset-db", action="store_true", help="Clear the database before seeding",
        )

    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError(
                "Do not seed in production! If in development change DEBUG to True and try again."
            )

        if options["reset_db"] and 'sqlite' not in settings.DATABASES['default']['ENGINE']:
            execute_from_command_line(["manage.py", "flush", "--no-input"])

        self._create_core(
            facebook_key=options.get("facebook_key"), facebook_secret=options.get("facebook_secret")
        )
        self._create_admin(create=options["admin"])

        self.stdout.write(self.style.SUCCESS("Seeded!"))

    def _create_core(self, facebook_key, facebook_secret):
        site = Site(id=1, name="localhost", domain="localhost:8000")
        site.save()

        if facebook_key and facebook_secret:
            social_app = SocialApp(
                id=1,
                provider="facebook",
                name="Facebook",
                client_id=facebook_key,
                secret=facebook_secret,
            )
            social_app.save()
            social_app.sites.add(site)

    def _create_admin(self, create):
        if not create:
            return None

        password = User.objects.make_random_password()

        try:
            User.objects.create_superuser("admin", "mail@example.com", password)
        except IntegrityError:
            raise CommandError("admin user already exists.")
        else:
            self.stdout.write(
                self.style.SUCCESS(f"Created superuser\nusername: admin\npassword: {password}")
            )
