from urllib.parse import quote

def encode_url(url: str) -> str:
   encoded_data = quote(url, safe="/:?=")
   return encoded_data