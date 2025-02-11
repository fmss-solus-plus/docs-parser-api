from django.urls import path
from .views import upload_doc_file, upload_doc_fileurl

urlpatterns = [
    path("upload-file/", upload_doc_file, name="upload_file"),
    path("upload-fileurl/", upload_doc_fileurl, name="upload_fileurl"),
]