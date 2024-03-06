from unittest.mock import patch
from django.test import TestCase
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile
from devices.factories import DeviceFactory
from observatories.factories import ObservatoryFactory
from services.csv_service import process_csv
from sightings.models.sighting import Sighting

class CsvServiceTests(TestCase):

    @patch('services.asteroid_detection_service.detect_asteroid')
    def test_process_csv(self, mock_detection_func):
        mock_detection_func.return_value = None

        device_id = uuid.uuid4()
        observatory_id = uuid.uuid4()
        r_height = 4
        r_width = 2

        DeviceFactory.create(id=device_id, r_height=r_height, r_width=r_width)
        ObservatoryFactory.create(id=observatory_id)

        csv_content = "datetime,device_resolution,observatory_code,device_code,device_matrix\n"
        csv_content += f"2022-01-01 12:00:00,{r_width}x{r_height},{observatory_id},{device_id},10101010\n"

        csv_file = SimpleUploadedFile("test_file.csv", csv_content.encode(), content_type="text/csv")

        # Ensure the process_csv function is working as expected
        process_csv(csv_file)

        # Check if the Sighting instance has been created in the database
        sighting_count = Sighting.objects.count()
        self.assertEqual(sighting_count, 1)

        # Retrieve the created Sighting instance and verify its attributes
        created_sighting = Sighting.objects.first()
        self.assertEqual(created_sighting.datetime.strftime('%Y-%m-%d %H:%M:%S'), "2022-01-01 12:00:00")
        self.assertEqual(created_sighting.observatory_id, observatory_id)
        self.assertEqual(created_sighting.device_id, device_id)
        self.assertEqual(created_sighting.device_matrix, "10101010")

    
        csv_file.close()

    @patch('services.asteroid_detection_service.detect_asteroid')
    def test_process_csv_error(self, mock_detection_func):
        mock_detection_func.side_effect = ValueError('Mocked error')
        
        device_id = uuid.uuid4()
        observatory_id = uuid.uuid4()
        r_height = 4
        r_width = 2

        DeviceFactory.create(id=device_id, r_height=r_height, r_width=r_width)
        ObservatoryFactory.create(id=observatory_id)

        csv_content = "datetime,device_resolution,observatory_code,device_code,device_matrix\n"
        csv_content += f"2022-01-01 12:00:00,{r_width}x{r_height},{observatory_id},{device_id},101010100000000\n" # device matrix is too long

        csv_file = SimpleUploadedFile("test_file.csv", csv_content.encode(), content_type="text/csv")

        with self.assertRaises(ValueError):
            process_csv(csv_file)
    
        csv_file.close()