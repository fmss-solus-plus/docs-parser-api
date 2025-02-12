import api.utils.openai_api.prompt_template as prompts

def template_create(doc_type: str):
    return (f"{prompts.SYSTEM_TEMPLATE}{prompts.RECOMMENDED_DOCUMENTS_LISTS[doc_type]}{prompts.HARDENING_TEMPLATE}"
            if doc_type in prompts.RECOMMENDED_DOCUMENTS_LISTS else None)