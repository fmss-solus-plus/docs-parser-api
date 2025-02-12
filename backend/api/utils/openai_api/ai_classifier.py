from openai import OpenAI
import json
import prompt_template as prompt_file
from dotenv import load_dotenv

import os
load_dotenv('.env')
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")

def openai_pdf_parser(resume_text):
    openai_api = OpenAI(api_key=AZURE_OPENAI_API_KEY)

    messages = [
        {"role": "system",
         "content": prompt_file.SYSTEM_TEMPLATE}
    ]

    user_info = resume_text

    messages.append({"role": "user", "content": user_info}) 

    response = openai_api.chat.completions.create(
               model="gpt-3.5-turbo",
               messages=messages,
               temperature=0.9,
               max_tokens=1000,
    )
    print("(PROMPT TOKENS) tokens used from requesting mesage -", response['usage']['prompt_tokens'])
    print("(COMPLETION TOKENS) tokens used when generating response -", response['usage']['completion_tokens'])
    print("TOTAL TOKENS USED-", response['usage']['total_tokens'])
    data = response.choices[0].message.content
    print(data)
    return data
    