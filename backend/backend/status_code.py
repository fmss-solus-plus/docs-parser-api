from rest_framework import status

STATUS_CODES = {
    "ERRORS": {
        400: status.HTTP_400_BAD_REQUEST,
        401: status.HTTP_401_UNAUTHORIZED,
        404: status.HTTP_404_NOT_FOUND,
        415: status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
    },
    "SUCCESS": {
        200: status.HTTP_200_OK,
        201: status.HTTP_201_CREATED,
        202: status.HTTP_202_ACCEPTED,
    }
}

STATUS_MESSAGES = {
    "ERRORS": {
        "NO_USERNAME_PASSWORD": "Username and password required",
        "EXISTS_USERNAME": "Username already exist",
        "INVALID_CREDENTIALS": "Invalid Credentials",
     },
    "SUCCESS": {
        "USER_REGISTERED": "Username registered successfully",
        "LOGIN_SUCCESSFUL": "Login successful",
    }
}