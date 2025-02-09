import requests
from io import BytesIO
from paddleocr import PaddleOCR
from pdf2image import convert_from_bytes
import numpy as np
import cv2
from dotenv import load_dotenv
import os
# from app.utils.openai.create_template import create_template
load_dotenv('.env')

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en', rec_algorithm='CRNN',
                det_db_box_thresh=0.6, det_db_unclip_ratio=1.5)


def download_file(request):
    data = request.json
    if 'fileUrl' not in data:
        print("No file URL provided")
        return "No file URL provided"

    file_url = data['fileUrl']

    try:
        response = requests.get(file_url, timeout=10)
        if response.status_code != 200:
            print("Failed to download the file")
            return "Failed to download the file"
        
        content_type = response.headers.get('Content-Type', '')
        if 'pdf' not in content_type:
            print("Only PDF files are supported")
            return "Only PDF files are supported"
        
        file = BytesIO(response.content)
        return file
    except Exception as e:
        return str(e)
    

def doc_parse(file):
    document_template = ''
    pdf_bytes = file.read()
    POPPLER_PATH = os.getenv('POPPLER_PATHS')

    # Convert PDF to images
    pages = convert_from_bytes(pdf_bytes, dpi=300, poppler_path=POPPLER_PATH)

    extracted_text = ''
    for page in pages:
        # Convert the PIL image to OpenCV format (required by PaddleOCR)
        img = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)

        # Run OCR
        result = ocr.ocr(img, cls=True)

        # Process and extract text from the result
        for line in result[0]:
            for word_info in line:
                if isinstance(word_info[0], str):
                    if document_template == '':
                        document_template = create_template(word_info[0])
                    extracted_text += word_info[0] + '\n'
    return extracted_text, document_template

