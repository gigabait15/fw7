from django.core.management import BaseCommand
from users.models import ServiceClient

class Command(BaseCommand):

    def handle(self, *args, **options):
        user = ServiceClient.objects.create(
            email='Admin@admin.pro',
            full_name='Admin',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password('Admin')
        user.save()