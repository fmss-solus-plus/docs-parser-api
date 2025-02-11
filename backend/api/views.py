from django.contrib.auth.decorators import login_required
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from .utils.document_parsing import download_file
from .utils.url_formatter import encode_url
from .serializers import DocumentUploadSerializer, DocumentUrlSerializer
from backend.status_code import STATUS_CODES, STATUS_MESSAGES

@extend_schema(
    summary="Upload a document for processing",
    description="Uploads a file, process it, and returns the classification and extracted text.",
    request=DocumentUploadSerializer,
    responses={
        STATUS_CODES["success"][200]: OpenApiResponse(
            description=f'{STATUS_MESSAGES["success"]["FILE_PROCESSED"]}',
            response=OpenApiTypes.OBJECT
        ),
        STATUS_CODES["errors"][400]: OpenApiResponse(
            description=f'{STATUS_MESSAGES["errors"]["INVALID_FILE_FORMAT"]}',
            response=OpenApiTypes.OBJECT
        ),
        STATUS_CODES["errors"][401]: OpenApiResponse(
            description=f'{STATUS_MESSAGES["errors"]["AUTH_REQUIRED"]}',
            response=OpenApiTypes.OBJECT
        ),
        }
)
@api_view(['POST'])
@parser_classes([MultiPartParser])
@login_required
def upload_doc_file(request):
    serializer = DocumentUploadSerializer(data=request.data)
    if serializer.is_valid():
        result = download_file(request)
        return Response({"message": f'{STATUS_MESSAGES["success"]["FILE_PROCESSED"]}',
                         "extracted_file": result},
                         status=STATUS_CODES["success"][200])
    return Response({"message": f'{STATUS_MESSAGES["errors"]["INVALID_FILE_FORMAT"]}'},
                     status=STATUS_CODES["errors"][400])


@extend_schema(
    summary="Upload a document URL for processing",
    description="Uploads a file URL, process it, and returns the classification and extracted text.",
    request=DocumentUrlSerializer,
    examples=[
        OpenApiExample(
            name="Request",
            value={"file_url": "https://example.com/file.pdf"},
            request_only=True
        )
    ],
    responses={
        STATUS_CODES["success"][200]: OpenApiResponse(
            description=f'{STATUS_MESSAGES["success"]["FILE_PROCESSED"]}',
            response=OpenApiTypes.OBJECT
        ),
        STATUS_CODES["errors"][400]: OpenApiResponse(
            description=f'{STATUS_MESSAGES["errors"]["INVALID_FILE_FORMAT"]}',
            response=OpenApiTypes.OBJECT
        ),
        STATUS_CODES["errors"][401]: OpenApiResponse(
            description=f'{STATUS_MESSAGES["errors"]["AUTH_REQUIRED"]}',
            response=OpenApiTypes.OBJECT
        ),
        }
)
@api_view(['POST'])
@login_required
def upload_doc_fileurl(request):
    data = request.data.get("file_url")
    encoded_data = encode_url(url=data)
    serializer = DocumentUrlSerializer(data={'file_url': encoded_data})
    if serializer.is_valid():
        file_url = serializer.validated_data['file_url']
        result = download_file(file_url)
        return Response({"message": f'{STATUS_MESSAGES["success"]["FILE_PROCESSED"]}',
                         "extracted_file": result},
                         status=STATUS_CODES["success"][200])
    return Response({"message": f'{STATUS_MESSAGES["errors"]["INVALID_FILE_FORMAT"]}'},
                     status=STATUS_CODES["errors"][400])