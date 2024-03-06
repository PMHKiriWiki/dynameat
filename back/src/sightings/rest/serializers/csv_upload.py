from commons.rest.fast_serializer import FastSerializer, FileField

class CSVUploadSerializer(FastSerializer):
    csv_file = FileField()