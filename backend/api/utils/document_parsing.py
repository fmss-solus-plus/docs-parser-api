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
    extracted_text = []

    segments = segment_image(page)

    ocr = PaddleOCR(
        use_angle_cls=True,
        lang="en",
        rec_algorithm="CRNN",
        det_db_box_thresh=0.6,
        det_db_unclip_ratio=1.5,
        use_gpu=True  # Enable GPU acceleration
    )

    for segment in segments:
        result = ocr.ocr(np.array(segment))  # Perform OCR on the image

        if result and isinstance(result, list) and isinstance(result[0], list):
            for line in result[0]:
                if isinstance(line, list) and len(line) > 1 and isinstance(line[1], tuple):
                    text = line[1][0]  # Extract the recognized word
                    extracted_text.append(text)

    del ocr
    gc.collect()
    return extracted_text

def segment_image(image):
    """Segment an image into smaller text regions using OpenCV"""
    print("Segmenting image...")
    image_np = np.array(image)
    gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    # edged = cv2.Canny(gray, 30, 150)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Detect text regions
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    segments = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if h > 10 and w > 10:
            segment = image.crop((x, y, x + w, y + h))
            segments.append(segment)

    return segments


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

    end_time = time.time()
    print(f"Document parsing took {end_time - start_time:.2f} seconds.")

    return extracted_text

