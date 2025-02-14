from openai import OpenAI
from dotenv import load_dotenv


import os
load_dotenv('.env')
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")

def openai_doc_classifier(resume_text: str, 
                          templates: str,
                          document_type: str):
    openai_api = OpenAI(api_key=AZURE_OPENAI_API_KEY)

    messages = [
        {"role": "system",
         "content": templates}
    ]

    user_info = resume_text
    openai_model = "gpt-3.5-turbo"

    messages.append({"role": "user", "content": user_info}) 

    response = openai_api.chat.completions.create(
               model=openai_model,
               messages=messages,
               temperature=0.9,
               max_tokens=1000,
    )
    total_tokens = response.usage.total_tokens
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens

    data = response.choices[0].message.content

    return data
