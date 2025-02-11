from rest_framework import serializers
from django.core.validators import URLValidator

class DocumentUploadSerializer(serializers.Serializer):
    file = serializers.FileField(
        required=False,
        help_text="Document file to upload"
    )

class DocumentUrlSerializer(serializers.Serializer):
    file_url = serializers.URLField(
        required=True,
        validators=[URLValidator(schemes=['http', 'https'])],
        help_text="URL of the document to process"
    )