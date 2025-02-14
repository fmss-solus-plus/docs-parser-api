from rest_framework import status

STATUS_CODES = {
    "errors": {
        400: status.HTTP_400_BAD_REQUEST,
        401: status.HTTP_401_UNAUTHORIZED,
        404: status.HTTP_404_NOT_FOUND,
        415: status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        500: status.HTTP_500_INTERNAL_SERVER_ERROR
    },
    "success": {
        200: status.HTTP_200_OK,
        201: status.HTTP_201_CREATED,
        202: status.HTTP_202_ACCEPTED,
    }
}

STATUS_MESSAGES = {
    "errors": {
        "MISSING_CREDENTIALS": "Username and password are required.",
        "USERNAME_EXISTS": "The username already exists.",
        "INVALID_CREDENTIALS": "Invalid username or password.",
        "INVALID_FILE_FORMAT": "Unsupported file format.",
        "AUTH_REQUIRED": "Authentication credentials are missing.",
        "INVALID_FILE_URL": "The provided file URL is invalid.",
        "FAILED_DOWNLOAD": "Failed to download the file.",
        "UNSUPPORTED_FILE_FORMAT": "Unsupported file format.",
        "UNSUPPORTED_DOCUMENT_FORMAT": "Unsupported document format provided."
    },
    "success": {
        "USER_REGISTERED": "User registered successfully.",
        "LOGIN_SUCCESSFUL": "Login successful.",
        "FILE_PROCESSED": "File processed successfully."
    }
}