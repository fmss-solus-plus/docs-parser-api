from django.contrib.auth.decorators import login_required
from drf_spectacular.utils import extend_schema, OpenApiResponse
from drf_spectacular.types import OpenApiTypes
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from .utils.document_parsing import download_file, doc_parse
from .utils.url_formatter import encode_url
from .serializers import DocumentUploadSerializer, DocumentUrlSerializer
from backend.status_code import STATUS_CODES, STATUS_MESSAGES
from api.utils.openai_api.template_builder import template_create, template_create_2
from api.utils.openai_api.ai_classifier import openai_doc_classifier
import time


@extend_schema(
    summary="Upload a document for processing",
    description="Uploads a file, process it, and returns the classification and extracted text.",
    request=DocumentUploadSerializer,
    responses={
        STATUS_CODES["success"][200]: OpenApiResponse(
            description=f'{STATUS_MESSAGES["success"]["FILE_PROCESSED"]}',
            response=OpenApiTypes.OBJECT,
        ),
        STATUS_CODES["errors"][400]: OpenApiResponse(
            description=f'{STATUS_MESSAGES["errors"]["INVALID_FILE_FORMAT"]}',
            response=OpenApiTypes.OBJECT,
        ),
        STATUS_CODES["errors"][401]: OpenApiResponse(
            description=f'{STATUS_MESSAGES["errors"]["AUTH_REQUIRED"]}',
            response=OpenApiTypes.OBJECT,
        ),
    },
)
@api_view(["POST"])
@parser_classes([MultiPartParser])
@login_required
def upload_doc_file(request):
    start_time = time.time()
    data = request.data

    serializer = DocumentUploadSerializer(data=data)

    if serializer.is_valid():
        doc_type = serializer.validated_data["document_type"]

        templates = template_create(
            doc_type=doc_type,
            template_corrections=serializer.validated_data["template_corrections"],
        )

        if templates is None:
            return Response(
                {
                    "message": f'{STATUS_MESSAGES["errors"]["UNSUPPORTED_DOCUMENT_FORMAT"]}'
                },
                status=STATUS_CODES["errors"][400],
            )

        file = serializer.validated_data["file"]

        parsed_file = doc_parse(file=file)

        # DO OPENAI INTEGRATION HERE
        result = openai_doc_classifier(
            resume_text=parsed_file, templates=templates, document_type=doc_type
        )
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Document parsing took {elapsed_time:.2f} seconds.")

        return Response(
            {
                "message": f'{STATUS_MESSAGES["success"]["FILE_PROCESSED"]}',
                "extracted_file": result,
            },
            status=STATUS_CODES["success"][200],
        )
    return Response(
        {"message": f'{STATUS_MESSAGES["errors"]["INVALID_FILE_FORMAT"]}'},
        status=STATUS_CODES["errors"][400],
    )


@extend_schema(
    summary="Upload a document URL for processing",
    description="Uploads a file URL, process it, and returns the classification and extracted text.",
    request=DocumentUrlSerializer,
    responses={
        STATUS_CODES["success"][200]: OpenApiResponse(
            description=f'{STATUS_MESSAGES["success"]["FILE_PROCESSED"]}',
            response=OpenApiTypes.OBJECT,
        ),
        STATUS_CODES["errors"][400]: OpenApiResponse(
            description=f'{STATUS_MESSAGES["errors"]["INVALID_FILE_FORMAT"]}',
            response=OpenApiTypes.OBJECT,
        ),
        STATUS_CODES["errors"][401]: OpenApiResponse(
            description=f'{STATUS_MESSAGES["errors"]["AUTH_REQUIRED"]}',
            response=OpenApiTypes.OBJECT,
        ),
    },
)
@api_view(["POST"])
@parser_classes([MultiPartParser])
@login_required
def upload_doc_fileurl(request):
    start_time = time.time()

    file_url_data = request.data.get("file_url")
    doc_type_data = request.data.get("document_type")
    template_correction_data = request.data.get("template_corrections")

    encoded_data = encode_url(url=file_url_data)
    serializer_dict = {
        "file_url": encoded_data,
        "document_type": doc_type_data,
        "template_corrections": template_correction_data,
    }

    serializer = DocumentUrlSerializer(data=serializer_dict)

    if serializer.is_valid():
        doc_type = serializer.validated_data["document_type"]

        templates = template_create_2(
            doc_type=doc_type,
            template_corrections=serializer.validated_data["template_corrections"],
        )
        print("TEMPLATES: ", templates)
        if templates is None:
            return Response(
                {
                    "message": f'{STATUS_MESSAGES["errors"]["UNSUPPORTED_DOCUMENT_FORMAT"]}'
                },
                status=STATUS_CODES["errors"][400],
            )
        file_url = serializer.validated_data["file_url"]
        downloaded_file = download_file(file_url=file_url)

        if not downloaded_file:
            return Response(
                {"message": STATUS_MESSAGES["errors"]["FAILED_DOWNLOAD"]},
                status=STATUS_CODES["errors"][400],
            )

        parsed_file = doc_parse(file=downloaded_file)

        # DO OPENAI INTEGRATION HERE
        result = openai_doc_classifier(
            resume_text=parsed_file, templates=templates, document_type=doc_type
        )
        print("PARSED_FILEEE: ", parsed_file)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Document parsing took {elapsed_time:.2f} seconds.")

        return Response(
            {
                "message": f'{STATUS_MESSAGES["success"]["FILE_PROCESSED"]}',
                "extracted_file": result,
            },
            status=STATUS_CODES["success"][200],
        )
    return Response(
        {"message": f'{STATUS_MESSAGES["errors"]["INVALID_FILE_FORMAT"]}'},
        status=STATUS_CODES["errors"][400],
    )
