import os
import random
from sys import exit

from datetime import datetime

import logging
from django.core.management.base import BaseCommand
from wapi.models import Weather

timestamp = datetime.now().strftime("%Y-%m-%d")

logger = logging.getLogger()
logging.basicConfig(
    filename=f'weather_data_load_{timestamp}.log',
    filemode='w', format='%(name)s - %(levelname)s - %(message)s'
)
logger.setLevel(logging.DEBUG)


class Command(BaseCommand):
    help = """
        Command to Load weather data to Database from a file or directory of files
        Check for duplicates: if your code is run twice, 
        you should not end up with multiple rows with the same data in your database. 
        Your code should also produce log output indicating start and end times and number of records ingested.
    """

    def add_arguments(self, parser):
        parser.add_argument('--directory', help="Directory of weather information files in .txt format")

    def handle(self, *args, **options):
        directory = options.get('directory')
        logger.debug(f"Started processing the files inside directory : {directory}")
        start_time = datetime.now()
        files = os.listdir(directory)

        if not files:
            logger.debug("No Files in the directory")
            exit(1)

        logger.debug(f"Timestamp for Starting process :: {start_time}")
        files = [os.path.join(directory, row) for row in files]
        Command.processing(files)
        end_time = datetime.now()
        logger.debug(f"Timestamp for Ending process :: {end_time}")
        c = start_time - end_time
        minutes = c.total_seconds() / 60
        logger.debug(f"Total difference in minutes: {minutes}")

    @staticmethod
    def processing(files):
        stations = ['Nebraska', 'Iowa', 'Illinois', 'Indiana', 'Ohio']
        for row in files:
            logger.debug(f"Started Reading the File :: {row}")
            data = open(row)
            for record in data:
                station = random.choice(stations)
                result = record.strip().split("\t")
                result = [rec.strip() for rec in result]
                date_object = datetime.strptime(result[0], '%Y%m%d').date()
                try:
                    Weather.objects.create(
                        **{
                            "tdate": date_object,
                            "max_temp": result[1] if result[1] != '-9999' else None,
                            "min_temp": result[2] if result[2] != '-9999' else None,
                            "amount": result[3] if result[3] != '-9999' else None,
                            "station": station
                        }
                    )
                except Exception as e:
                    logger.error(f"Unique Key Constraint Failed :: {row} -- {result}")
