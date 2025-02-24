from rest_framework.response import Response
from io import BytesIO
from typing import BinaryIO
from paddleocr import PaddleOCR
from pdf2image import convert_from_bytes
from backend.status_code import STATUS_CODES, STATUS_MESSAGES
from backend.settings import POPPLER_PATH

import numpy as np
import cv2
import requests
import time
import gc

# Initialize PaddleOCR (Enable GPU if available)

def download_file(file_url: str):
    try:
        response = requests.get(file_url, timeout=3)
        if response.status_code != 200:
            return Response(
                {"message": STATUS_MESSAGES["errors"]["FAILED_DOWNLOAD"]},
                status=STATUS_CODES["errors"][400],
            )

        content_type = response.headers.get("Content-Type", "")
        if "pdf" not in content_type:
            return Response(
                {"message": STATUS_MESSAGES["errors"]["UNSUPPORTED_FILE_FORMAT"]},
                status=STATUS_CODES["errors"][415],
            )
        return BytesIO(response.content)
    except Exception as e:
        return Response({"message": str(e)}, status=STATUS_CODES["errors"][500])


def process_page(page):
    """Process a single page using OCR and extract text."""
    print("PROCESSING PAGE...")
    page = page.resize((int(page.width * 0.75), int(page.height * 0.75)))  # Resize to double the size
    img = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2GRAY)  # Convert to grayscale

    ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en",
    rec_algorithm="CRNN",
    det_db_box_thresh=0.6,
    det_db_unclip_ratio=1.5,
    use_gpu=True  # Enable GPU acceleration
    )
    
    result = ocr.ocr(img, cls=True)
    del ocr
    gc.collect()

    return " ".join(
        word_info[0]
        for line in result[0]
        for word_info in line
        if isinstance(word_info[0], str)
    )


def doc_parse(file: BinaryIO):
    start_time = time.time()
    pdf_bytes = file.read()

    # Convert PDF to images (Lower DPI to speed up conversion)
    all_pages = convert_from_bytes(pdf_bytes, dpi=100, poppler_path=POPPLER_PATH)

    print("START DOCUMENT PROCESSING...")
    # Process only the first page
    extracted_text = process_page(all_pages[0]) if all_pages else ""

    del pdf_bytes, all_pages
    gc.collect()

    print("EXTRACTED TEXT: ", extracted_text)
    end_time = time.time()
    print(f"Document parsing took {end_time - start_time:.2f} seconds.")

    return extracted_text

