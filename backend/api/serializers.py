from rest_framework import serializers
from django.core.validators import URLValidator
import api.utils.openai_api.prompt_template as prompts

class DocumentUploadSerializer(serializers.Serializer):
    file = serializers.FileField(
        required=True,
        help_text="Document file to upload"
    )

    document_type = serializers.ChoiceField(
        choices=[(key, key) for key in prompts.RECOMMENDED_DOCUMENTS_LISTS.keys()],  # Converts dict keys into choice tuples
        required=True,
        help_text="Select the document type"
    )

    template_corrections = serializers.CharField(
        required=False,
        help_text="Customize or refine the classifier's response by specifying corrections or modifications."
                  "Example: 'Do not use capital letters in names.'",
        style={'base_template': 'textarea.html'}
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

    template_corrections = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
        help_text="Customize or refine the classifier's response by specifying corrections or modifications."
                  "Example: 'Do not use capital letters in names.'",
        style={'base_template': 'textarea.html'}
    )
