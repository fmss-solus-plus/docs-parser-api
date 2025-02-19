from rest_framework.response import Response
from io import BytesIO
from typing import BinaryIO
from paddleocr import PaddleOCR
from pdf2image import convert_from_bytes
from concurrent.futures import ThreadPoolExecutor
from backend.status_code import STATUS_CODES, STATUS_MESSAGES
from backend.settings import POPPLER_PATH

import numpy as np
import cv2
import requests
import time

# Initialize PaddleOCR

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en",
    rec_algorithm="CRNN",
    det_db_box_thresh=0.6,
    det_db_unclip_ratio=1.5,
)


def download_file(file_url: str):
    try:
        response = requests.get(file_url, timeout=10)
        if response.status_code != 200:
            return Response(
                {"message": f'{STATUS_MESSAGES["errors"]["FAILED_DOWNLOAD"]}'},
                status=STATUS_CODES["errors"][400],
            )

        content_type = response.headers.get("Content-Type", "")
        if "pdf" not in content_type:
            return Response(
                {"message": f'{STATUS_MESSAGES["errors"]["UNSUPPORTED_FILE_FORMAT"]}'},
                status=STATUS_CODES["errors"][415],
            )
        file = BytesIO(response.content)
        return file
    except Exception as e:
        return Response({"message": f"{str(e)}"}, status=STATUS_CODES["errors"][500])


def process_page(page):
    """Process a single page using OCR and extract text."""
    img = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)
    result = ocr.ocr(img, cls=True)

    return " ".join(
        word_info[0]
        for line in result[0]
        for word_info in line
        if isinstance(word_info[0], str)
    )


def doc_parse(file: BinaryIO):
    start_time = time.time()
    pdf_bytes = file.read()

    # Convert PDF to images
    all_pages = convert_from_bytes(pdf_bytes, dpi=200, poppler_path=POPPLER_PATH)
    page_numbers_list = [1]
    pages = (
        [all_pages[i - 1] for i in page_numbers_list]
        if page_numbers_list
        else all_pages
    )

    extracted_text = ""
    with ThreadPoolExecutor() as executor:
        extracted_text = list(executor.map(process_page, pages))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Document parsing took {elapsed_time:.2f} seconds.")
    return " ".join(extracted_text)
