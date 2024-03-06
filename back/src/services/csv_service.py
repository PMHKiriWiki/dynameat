import logging
import csv
import io

from django.db import transaction
from services.asteroid_detection_service import detect_asteroid
from sightings.models.sighting import Sighting

logger = logging.getLogger(__name__)


def _read_csv_content(csv_file):
    csv_content = csv_file.read().decode('utf-8')
    
    csv_reader = csv.DictReader(io.StringIO(csv_content))

    data_list = list(csv_reader)
    return data_list


def _validate_sighting_data(sighting):
    required_fields = ['datetime', 'device_resolution', 'observatory_code', 'device_code', 'device_matrix']
    if not all(sighting.get(field) for field in required_fields):
        raise ValueError("Incomplete data in CSV row")

def _create_sighting_instance(sighting):
    device_matrix = sighting['device_matrix']
    datetime = sighting['datetime']
    device_resolution = sighting['device_resolution']
    observatory_id = sighting['observatory_code']
    device_id = sighting['device_code']

    device_resolution_width, device_resolution_height = map(int, device_resolution.split('x'))
    
    asteroid = detect_asteroid(device_matrix, device_resolution_width, device_resolution_height)

    return Sighting(
        datetime=datetime,
        observatory_id=observatory_id,
        device_id=device_id,
        asteroid_id=asteroid.id,
        device_matrix=device_matrix
    )

def process_csv(csv_file):
    data_list = _read_csv_content(csv_file)
    sightings_to_create = []

    for sighting_data in data_list:
        _validate_sighting_data(sighting_data)
        sighting_instance = _create_sighting_instance(sighting_data)
        sightings_to_create.append(sighting_instance)

    with transaction.atomic():
        Sighting.objects.bulk_create(sightings_to_create)