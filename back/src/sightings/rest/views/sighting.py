import logging
import os 

from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

from services.csv_service import process_csv

from ...models.sighting import Sighting
from ..serializers import SightingSerializer

logger = logging.getLogger(__name__)

class SightingView(GenericViewSet, ListModelMixin):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer


    @action(detail=False, methods=['POST'])
    def upload_file(self, request):
        try:
            # csv_file = request.data['file'] # TODO integration with frontend
            # process_csv(csv_file)

            csv_file = None
            local_csv_path = 'storage/sightings_1.csv'

            if os.path.exists(local_csv_path):
                  with open(local_csv_path, 'rb') as file:
                    csv_content = file.read()
                    csv_file = SimpleUploadedFile("local_file.csv", csv_content, content_type="text/csv")

            if csv_file:
                process_csv(csv_file)
                return Response({'message': 'File uploaded and processed successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Local CSV file not found'}, status=status.HTTP_404_NOT_FOUND)
    
        except ValueError as ve:
            return Response({'error': str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error processing CSV file: {str(e)}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)