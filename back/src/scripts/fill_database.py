
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_setup.settings")

import django
django.setup()

from django.db import transaction
from devices.models.device import Device

from observatories.models import Location, Observatory

def create_or_get_observatory(observatory_id, index):
    observatory, created = Observatory.objects.get_or_create(id=observatory_id, defaults={'name': f'Observatory_{index + 1}'})
    
    if created:
        # If the observatory is newly created, create a Location for it
        location = Location.objects.create(
            address=f"Address_{index + 1}",
            city=f"City_{index + 1}",
            country=f"Country_{index + 1}",
            phone=12345678
        )
        observatory.location = location
        observatory.save()

    return observatory

def create_or_get_device(device_id, device_resolutions, index):
    return Device.objects.get_or_create(
        id=device_id, name=f"Device_{index}", 
        defaults = {
            'r_weight': device_resolutions[index][0],
            'r_height': device_resolutions[index][1]
        })[0]

def create_data():
    # List of Observatory and Device IDs
    observatory_ids = [
      '0f6d13e5-6562-4b9a-8e31-3dc98b75c1a6',
      'b8a4ac31-f36f-4879-8db0-8ac104d7b1c5',
      '27f47c9f-83da-4f8a-9ba3-aa5e5c7a0f4d',
      '85d0a11a-2b04-4e77-8c2d-96a0f3f428bb',
      'c9329e38-56f5-4e0b-83d3-4ee13e944ff3',
      '3fe6dd78-4993-49e5-8e5f-23e1d3c8762a',
      'db5c048a-dcc9-4cf9-9234-9d0a3de238bf',
      '719583c1-0568-4aa5-87b3-5c05c8d0fb9e',
      'cf39ef12-bdf9-4cd5-bf14-4a95a768d165',
      '4e07ac45-5523-4870-a2ea-c9f6c887f215',
      'a9e6f9e1-c732-4d52-9aa6-28fb8ebf8c8a'
    ]

    device_ids = [
      'b0a6c975-2d71-4e19-bfa3-9a4773e1f987',
      'ef228ca2-bce4-4ed9-8a92-3e98441f7e11',
      '36c28922-bafe-41a8-8f3e-2f9c1c5c8f0a',
      'ce593fa2-607b-4cf4-846e-98d1a1f5bc45',
      'd4cc4019-6058-4a69-84ef-810e77f7eb36',
      '33c1b7e3-943d-41b4-aaec-92a3b0f64ef8',
      'a4f86035-d7a1-4b1f-b558-4ec1f916f4ad',
      'f5814b8a-1e0b-40c6-9d60-9c23ceca4a23',
      '422d6f98-762b-4291-b786-1a4337aa7885',
      '7c080d4f-14f2-4ef5-a1cb-6ac5c47bf1f5',
    ]

    device_resolutions = [
        (6, 3),
        (3, 4),
        (4, 5),
        (6, 4),
        (6, 6),
        (3, 7),
        (3, 5),
        (4, 4),
        (5, 5),
        (3, 3),
    ]

    # Create or get Observatories and Devices based on fixed IDs
    observatories = [create_or_get_observatory(observatory_id, index) for observatory_id, index in zip(observatory_ids, range(len(observatory_ids)))]
    devices = [create_or_get_device(device_id, device_resolutions, index) for device_id, index in zip(device_ids, range(len(device_ids)))]

    # Print information about created Observatories and Devices
    print("Created or existing Observatories:")
    for observatory in observatories:
        print(f"ID: {observatory.id}, Name: {observatory.name}")

    print("\nCreated or existing Devices:")
    for device in devices:
        print(f"ID: {device.id}, Name: {device.name}")

if __name__ == "__main__":

    with transaction.atomic():
        create_data()
