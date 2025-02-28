"""
    This is file contains functions that reformat the url of the uploaded files.
"""
from urllib.parse import quote


def encode_url(url: str) -> str:
    return url if "%" in url else quote(url, safe="/:?=")
