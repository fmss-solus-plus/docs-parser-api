import api.utils.openai_api.prompt_template as prompts

def template_create(doc_type: str, template_corrections: str = None):
    if doc_type not in prompts.RECOMMENDED_DOCUMENTS_LISTS:
        return None  # Return None if doc_type is invalid

    # Construct the template with corrections placed between HARDENING_TEMPLATE and RECOMMENDED_DOCUMENTS_LISTS
    template = (
        f"{prompts.SYSTEM_TEMPLATE}"
        f"{prompts.HARDENING_TEMPLATE}"
        f"Prioritize extracting the values listed under this corresponding list:\n{prompts.RECOMMENDED_DOCUMENTS_LISTS[doc_type]}"
    )
    if 'NAME' in prompts.RECOMMENDED_DOCUMENTS_LISTS[doc_type]:
        template += f"\n{prompts.SPECIALIZED_TEMPLATE['NAME']}"
    if 'VALIDITY_DATE' in prompts.RECOMMENDED_DOCUMENTS_LISTS[doc_type]:
        template += f"\n{prompts.SPECIALIZED_TEMPLATE['VALIDITY_DATE']}"
    if template_corrections:
        template += f"\n{template_corrections}"

    return template