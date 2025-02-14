from urllib.parse import quote, unquote


def encode_url(url: str) -> str:
    return url if "%" in url else quote(url, safe="/:?=")
