from openai import OpenAI
from api.models import OpenAIRequest
from backend.settings import AZURE_OPENAI_API_KEY


def openai_doc_classifier(resume_text: str, templates: str, document_type: str):
    openai_api = OpenAI(api_key=AZURE_OPENAI_API_KEY)
    messages = [{"role": "system", "content": templates}]

    user_info = resume_text

    openai_model = "gpt-3.5-turbo"

    messages.append({"role": "user", "content": user_info})

    response = openai_api.chat.completions.create(
        model=openai_model,
        messages=messages,
        temperature=1,
        top_p=1,
        max_tokens=1000,
        frequency_penalty=0,
        presence_penalty=0
    )

    total_tokens = response.usage.total_tokens

    prompt_tokens = response.usage.prompt_tokens

    completion_tokens = response.usage.completion_tokens

    add_ai_usage_logs(
        document_type=document_type,
        ai_model=openai_model,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        total_tokens=total_tokens,
    )

    data = response.choices[0].message.content

    return data


def add_ai_usage_logs(
    document_type: str,
    ai_model: str,
    prompt_tokens: int,
    completion_tokens: int,
    total_tokens: int,
):

    OpenAIRequest.objects.create(
        document_type=document_type,
        ai_model=ai_model,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        total_tokens=total_tokens,
    )
