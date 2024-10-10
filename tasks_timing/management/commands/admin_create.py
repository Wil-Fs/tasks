from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from dotenv import load_dotenv
import os

load_dotenv()

admin_user = os.getenv('ADMIN_USER')
admin_password = os.getenv('ADMIN_PASSWORD')
admin_email = os.getenv('ADMIN_EMAIL')


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username=admin_user).exists():
            User.objects.create_superuser(
                username=admin_user,
                email=admin_email,
                password=admin_password
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))
