from django.core.management.base import BaseCommand

from scripts.fill_database import create_data

class Command(BaseCommand):
    help = 'Fill the database with sample data'

    def handle(self, *args, **options):
        create_data()  # Call your script function
        self.stdout.write(self.style.SUCCESS('Database filled successfully'))
