import logging
from collections import defaultdict

from drf_spectacular.openapi import AutoSchema
from rest_framework.parsers import JSONParser
from rest_polymorphic.serializers import PolymorphicSerializer

from .fast_serializer import FastSerializer

logger = logging.getLogger(__name__)

class FastAutoSchema(AutoSchema):
    """
    AutoSchema to use with FastSerializer.
    """

    def _get_request_body(self):
        if self.method == 'GET':
            return {}

        serializer = self.get_response_serializers()

        if isinstance(serializer, PolymorphicSerializer):
            serializer = list(serializer.model_serializer_mapping.values())[0]

        if isinstance(serializer, FastSerializer):
            return {
                'content': {
                    self._get_content_type(): {
                        'schema': serializer.get_request_schema()
                    }
                }
            }
        else:
            return super()._get_request_body()

    def _get_content_type(self):
        return 'application/json' if JSONParser in self.view.parser_classes else 'multipart/form-data'

    def _get_response_bodies(self):
        serializer = self.get_response_serializers()

        if isinstance(serializer, PolymorphicSerializer):
            serializer = list(serializer.model_serializer_mapping.values())[0]

        if isinstance(serializer, FastSerializer):
            response_bodies = {
                200: {
                    'content': {
                        'application/json': {
                            'schema': serializer.get_response_schema()
                        }
                    }
                },
            }

            if hasattr(self.view, 'error_response_schemas'):
                response_bodies.update(self._build_error_response_schema())

            return response_bodies
        else:   
            return super()._get_response_bodies()

    def _build_error_response_schema(self):
        error_types_by_status_code = defaultdict(list)

        for error_response_squema in self.view.error_response_schemas:
            error_types_by_status_code[error_response_squema.status_code].append(error_response_squema.type)

        complete_error_response_squema = dict()

        for status_code, error_types in error_types_by_status_code.items():
            complete_error_response_squema[status_code] = {
                'content': {
                    'application/problem+json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'type': {
                                    'type': 'string',
                                    'description': 'A URI reference [RFC3986] that identifies the problem type. ',
                                    'enum': error_types,
                                }
                            },
                        }
                    }
                }
            }

        return complete_error_response_squema
