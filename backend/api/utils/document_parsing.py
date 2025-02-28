from rest_framework.response import Response
from io import BytesIO
from typing import BinaryIO
from paddleocr import PaddleOCR
from pdf2image import convert_from_bytes
from backend.status_code import STATUS_CODES, STATUS_MESSAGES
from backend.settings import POPPLER_PATH

import numpy as np
import requests
import time
import gc
import sys

ocr = None
if "makemigrations" not in sys.argv and "migrate" not in sys.argv:
    ocr = PaddleOCR(
        det_model_dir="api/utils/ai_models/en_PP-OCRv3_det_infer",  # Use English OCR model
        rec_model_dir="api/utils/ai_models/en_PP-OCRv3_rec_infer", 
        use_angle_cls=False,
        lang="en",
        rec_algorithm="CRNN",
        det_db_box_thresh=0.6,
        det_db_unclip_ratio=1.5,
        use_gpu=False  # Enable GPU acceleration
    )
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
        
        file_stream = BytesIO()
        for chunk in response.iter_content(chunk_size=4096):
            file_stream.write(chunk)
        
        file_stream.seek(0)
        return file_stream
    except Exception as e:
        return Response({"message": str(e)}, status=STATUS_CODES["errors"][500])

def process_page(page, ocr: PaddleOCR):
    """Process a single page using OCR and extract text."""
    print("PROCESSING PAGE...")
    page = page.convert("L")  # Convert to grayscale format
    scale_factor = 0.75
    resize_page = page.resize((int(page.width * scale_factor), int(page.height * scale_factor)))  # Resize to double the size
    img = np.array(resize_page)  # Convert to numpy array

    result = ocr.ocr(img)  # Perform OCR on the image

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
    extracted_text = []

    print("START DOCUMENT PROCESSING...")
    for page in convert_from_bytes(pdf_bytes, dpi=100, poppler_path=POPPLER_PATH):
        extracted_text.append(process_page(page=page, ocr=ocr))
        del page
        gc.collect()

    end_time = time.time()
    print(f"Document parsing took {end_time - start_time:.2f} seconds.")

    return " ".join(extracted_text)

