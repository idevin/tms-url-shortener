from django.core.management.base import BaseCommand
from django.db import connection
from shortener import settings


class Command(BaseCommand):
    help = 'Setup Mysql database for U.short'

    def handle(self, *args, **options):
        db_name = settings.DATABASES['default']['NAME']

        cursor = connection.cursor()
        cursor.execute('CREATE DATABASE %s', [db_name])
        connection.commit()
