import os
from abc import ABC
from uuid import UUID

import requests
from django.core.files import File
from django.core.files.base import ContentFile
from django.db.models import QuerySet
from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from django.db.models.fields.files import ImageField
from django.core.files import File

class Field(ABC):
    def __init__(self, read_only=False, *args, **kwargs):
        self.read_only = read_only

    def get_serialized_value(self, instance, field_name):
        raise NotImplementedError('`get_serialized_value(instance, field_name)` must be implemented.')

    def to_internal_value(self, value):
        raise NotImplementedError('`to_internal_value(value)` must be implemented.')

    def get_request_schema(self):
        raise NotImplementedError('`get_request_schema()` must be implemented.')

    def get_response_schema(self):
        raise NotImplementedError('`get_response_schema()` must be implemented.')


class CharField(Field):
    def get_serialized_value(self, instance, field_name):
        return getattr(instance, field_name)

    def to_internal_value(self, value):
        return value

    def get_request_schema(self):
        return self._get_schema()

    def get_response_schema(self):
        return self._get_schema()

    def _get_schema(self):
        return {
            'type': 'string',
        }


class IntegerField(Field):
    def get_serialized_value(self, instance, field_name):
        return getattr(instance, field_name)

    def to_internal_value(self, value):
        return int(value)

    def get_request_schema(self):
        return self._get_schema()

    def get_response_schema(self):
        return self._get_schema()

    def _get_schema(self):
        return {
            'type': 'integer',
        }
    
class FloatField(Field):
    def get_serialized_value(self, instance, field_name):
        return getattr(instance, field_name)

    def to_internal_value(self, value):
        return float(value)

    def get_request_schema(self):
        return self._get_schema()

    def get_response_schema(self):
        return self._get_schema()

    def _get_schema(self):
        return {
            'type': 'float',
        }

class BooleanField(Field):
    def get_serialized_value(self, instance, field_name):
        return getattr(instance, field_name)

    def to_internal_value(self, value):
        return value

    def get_request_schema(self):
        return self._get_schema()

    def get_response_schema(self):
        return self._get_schema()

    def _get_schema(self):
        return {
            'type': 'boolean',
        }


class DateTimeField(Field):
    def get_serialized_value(self, instance, field_name):
        datetime = getattr(instance, field_name)

        if datetime is None:
            return None

        return serializers.DateTimeField().to_representation(datetime)

    def to_internal_value(self, value):
        return serializers.DateTimeField().to_internal_value(value)

    def get_request_schema(self):
        return self._get_schema()

    def get_response_schema(self):
        return self._get_schema()

    def _get_schema(self):
        return {
            'type': 'string',
            'format': 'date-time',
        }


class FileField(Field):
    def get_serialized_value(self, instance, field_name):
        file_field = getattr(instance, field_name)

        return self.file_field_to_url(file_field)

    @staticmethod
    def file_field_to_url(file_field):
        try:
            return file_field.url if os.environ.get("ENV") != 'DEV' else f"{os.environ.get('BACKEND_URL')}:{os.environ.get('NGINX_EXTERNAL_PORT')}{file_field.url}"
        except:
            return None

    def to_internal_value(self, value):
        if isinstance(value, File):
            return value
        if isinstance(value, str):
            r = requests.get(value)
            return ContentFile(r.content, name=os.path.basename(value))
        return value

    def get_request_schema(self):
        return {
            'type': 'string',
            'format': 'binary',
        }

    def get_response_schema(self):
        return {
            'type': 'string',
            'format': 'uri',
        }


class UUIDField(Field):
    def get_serialized_value(self, instance, field_name):
        return str(getattr(instance, field_name))

    def to_internal_value(self, value):
        return value

    def get_request_schema(self):
        return self._get_schema()

    def get_response_schema(self):
        return self._get_schema()

    def _get_schema(self):
        return {
            'type': 'string',
            'format': 'uuid'
        }


class NestedSerializerField(Field):
    def __init__(self, serializer_class, *args, **kwargs):
        self.serializer_class = serializer_class

        super().__init__(*args, **kwargs)

    def get_serialized_value(self, instance, field_name):
        if hasattr(instance, field_name):
            related_model = getattr(instance, field_name)

            return None if related_model is None else self.serializer_class(related_model).data
        else:
            return None

    def to_internal_value(self, value):
        return value

    def get_request_schema(self):
        return UUIDField().get_request_schema()

    def get_response_schema(self):
        return self.serializer_class().get_response_schema()
    
class JSONField(Field):
    def get_serialized_value(self, instance, field_name):
        return getattr(instance, field_name)

    def to_internal_value(self, value):
        return value

    def get_request_schema(self):
        return self._get_schema()

    def get_response_schema(self):
        return self._get_schema()

    def _get_schema(self):
        return {
            'type': 'object',
            'format': 'json'
        }



class ForeignKeyField(Field):
    def get_serialized_value(self, instance, field_name):
        id = getattr(instance, f'{field_name}_id')

        if isinstance(id, UUID):
            return str(id)
        else:
            return id

    def to_internal_value(self, value):
        return value

    def get_request_schema(self):
        return self._get_schema()

    def get_response_schema(self):
        return self._get_schema()

    def _get_schema(self):
        return UUIDField().get_request_schema()


class FastSerializer:
    def __new__(cls, *args, **kwargs):
        cls.fields = {}

        for attribute in dir(cls):
            value = getattr(cls, attribute)

            if isinstance(value, Field):
                cls.fields[attribute] = value

        return super().__new__(cls)

    def __init__(self, instance=None, data=None, **kwargs):
        self.context = kwargs.pop('context', {})

        self.instance = instance
        if data is not None:
            self.initial_data = data

    def instance_to_representation(self, instance):
        return {field_name: field_object.get_serialized_value(instance, field_name) for field_name, field_object in self.fields.items()}

    @property
    def validated_data(self):
        response = dict()
        for key, value in self.initial_data.items():
            if key in self.fields and not self.fields[key].read_only:
                if isinstance(self.fields[key], NestedSerializerField) or isinstance(self.fields[key], ForeignKeyField):
                    response[f'{key}_id'] = self.fields[key].to_internal_value(value)
                else:
                    response[key] = self.fields[key].to_internal_value(value)

        self._validated_data = response

        return response

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def save(self, **kwargs):
        validated_data = {**self.validated_data, **kwargs}

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)

        return self.instance

    def is_valid(self, raise_exception=False):
        return True

    @property
    def data(self):
        return self.to_representation(self.instance)

    @classmethod
    def image_field_to_thumbnail_url(cls, image_field, size_str):
        try:
            return FileField.file_field_to_url(get_thumbnail(image_field, size_str, crop="center", quality=100))
        except:
            return None

    def serialize_datetime(self, datetime):
        if datetime is None:
            return None

        return serializers.DateTimeField().to_representation(datetime)

    def to_representation(self, instance):
        if isinstance(instance, QuerySet) or isinstance(instance, list):
            return [self.instance_to_representation(i) for i in instance]
        else:
            return self.instance_to_representation(instance)

    def get_request_schema(self):
        return self._get_schema(self._get_schema_request_properties)

    def get_response_schema(self):
        return self._get_schema(self._get_schema_response_properties)

    def _get_schema(self, get_schema_properties_method):
        schema = {
            'type': 'object',
            'properties': get_schema_properties_method()
        }

        return schema

    def _get_schema_request_properties(self):
        properties = dict()

        for field_name, field_object in self.fields.items():
            if field_object.read_only:
                continue

            properties[field_name] = field_object.get_request_schema()

        return properties

    def _get_schema_response_properties(self):
        properties = dict()

        for field_name, field_object in self.fields.items():
            properties[field_name] = field_object.get_response_schema()

        return properties
