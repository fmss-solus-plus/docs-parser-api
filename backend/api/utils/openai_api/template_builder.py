import api.utils.openai_api.prompt_template as prompts

def template_create(doc_type):
    templates = ''
    if doc_type in prompts.RECOMMENDED_DOCUMENTS_LISTS:
        templates = f"""
        {prompts.SYSTEM_TEMPLATE}
        {prompts.RECOMMENDED_DOCUMENTS_LISTS.get(doc_type)}
        {prompts.HARDENING_TEMPLATE}
        """
        return templates
    return None