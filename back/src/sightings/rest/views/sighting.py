import logging

from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from services.csv_service import process_csv

from ...models.sighting import Sighting
from ..serializers import SightingSerializer, CSVUploadSerializer


logger = logging.getLogger(__name__)

class SightingView(GenericViewSet, ListModelMixin):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer


    @action(detail=False, methods=['POST'])
    def upload_file(self, request):
        try:
            csv_file = request.data['file']
            process_csv(csv_file)
            return Response({'message': 'File uploaded and processed successfully'}, status=status.HTTP_201_CREATED)
        except ValueError as ve:
            return Response({'error': str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error processing CSV file: {str(e)}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)