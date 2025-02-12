from rest_framework import serializers
from django.core.validators import URLValidator
import api.utils.openai_api.prompt_template as prompts

class DocumentUploadSerializer(serializers.Serializer):
    file = serializers.FileField(
        required=False,
        help_text="Document file to upload"
    )

    document_type = serializers.ChoiceField(
        choices=[(key, key) for key in prompts.RECOMMENDED_DOCUMENTS_LISTS.keys()],  # Converts dict keys into choice tuples
        required=True,
        help_text="Select the document type"
    )

class DocumentUrlSerializer(serializers.Serializer):
    file_url = serializers.URLField(
        required=True,
        validators=[URLValidator(schemes=['http', 'https'])],
        help_text="URL of the document to process"
    )

    document_type = serializers.ChoiceField(
        choices=[(key, key) for key in prompts.RECOMMENDED_DOCUMENTS_LISTS.keys()],  # Converts dict keys into choice tuples
        required=True,
        help_text="Select the document type"
    )
