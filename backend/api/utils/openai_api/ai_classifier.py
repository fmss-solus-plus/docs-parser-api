from openai import OpenAI
from dotenv import load_dotenv

import os
load_dotenv('.env')
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")

def openai_doc_classifier(resume_text: str, templates: str):
    openai_api = OpenAI(api_key=AZURE_OPENAI_API_KEY)

    messages = [
        {"role": "system",
         "content": templates}
    ]

    user_info = resume_text

    messages.append({"role": "user", "content": user_info}) 
    print("############## MESSAGES ##############: ", messages)
    response = openai_api.chat.completions.create(
               model="gpt-3.5-turbo",
               messages=messages,
               temperature=0.9,
               max_tokens=1000,
    )
    print("(PROMPT TOKENS) tokens used from requesting message -", response.usage.prompt_tokens)
    print("(COMPLETION TOKENS) tokens used when generating response -", response.usage.completion_tokens)
    print("TOTAL TOKENS USED -", response.usage.total_tokens)
    data = response.choices[0].message.content

    return data
    