import api.utils.openai_api.prompt_template as prompts


def template_create(doc_type: str, template_corrections: str = None):
    if doc_type not in prompts.RECOMMENDED_DOCUMENTS_LISTS:
        return None  # Return None if doc_type is invalid

    system_template = build_template(
        doc_type=doc_type, template=prompts.SYSTEM_TEMPLATE
    )

    hardening_template = build_template(
        doc_type=doc_type, template=prompts.HARDENING_TEMPLATE
    )

    # Construct the template with corrections placed between HARDENING_TEMPLATE and RECOMMENDED_DOCUMENTS_LISTS
    template = (
        f"{system_template}"
        f"{hardening_template}"
        f"\nPrioritize extracting the values listed under this corresponding list:\n{prompts.RECOMMENDED_DOCUMENTS_LISTS[doc_type]}"
    )
    if "NAME" in prompts.RECOMMENDED_DOCUMENTS_LISTS[doc_type]:
        template += f"{prompts.SPECIALIZED_TEMPLATE['NAME']}"
    if "VALIDITY_DATE" in prompts.RECOMMENDED_DOCUMENTS_LISTS[doc_type]:
        template += f"{prompts.SPECIALIZED_TEMPLATE['VALIDITY_DATE']}"
    if "VISA_TYPE" in prompts.RECOMMENDED_DOCUMENTS_LISTS[doc_type]:
        template += f"{prompts.SPECIALIZED_TEMPLATE['VISA_TYPE']}"
    if "SHIP/PROJECT_DEPARTMENT_LEVEL" in prompts.RECOMMENDED_DOCUMENTS_LISTS[doc_type]:
        template += f"{prompts.SPECIALIZED_TEMPLATE['SHIP_PROJECT_DEPARTMENT_LEVEL']}"
    if template_corrections:
        template += f"{template_corrections}"

    return template


def build_template(doc_type: str, template: str) -> str:
    return template.replace("[*doc_type*]", doc_type)

def build_required_docs_template(required_docs: str, template: str) -> str:
    return template.replace("[*required_docs*]", required_docs)


def template_create_2(doc_type: str, template_corrections: str = None):
    if doc_type not in prompts.RECOMMENDED_DOCUMENTS_LISTS_2:
        return None  # Return None if doc_type is invalid

    system_template = build_template(
        doc_type=doc_type, template=prompts.SYSTEM_TEMPLATE_2
    )

    system_template = build_required_docs_template(required_docs=prompts.RECOMMENDED_DOCUMENTS_LISTS_2[doc_type], template=system_template)
    
    hardening_template = build_template(
        doc_type=doc_type, template=prompts.HARDENING_TEMPLATE_2
    )

    # Construct the template with corrections placed between HARDENING_TEMPLATE and RECOMMENDED_DOCUMENTS_LISTS
    template = (
        f"{system_template}"
        f"{hardening_template}"
    )
    if "NAME" in prompts.RECOMMENDED_DOCUMENTS_LISTS_2[doc_type]:
        template += f"{prompts.SPECIALIZED_TEMPLATE_2['NAME']}"
    if "VALIDITY_DATE" in prompts.RECOMMENDED_DOCUMENTS_LISTS_2[doc_type]:
        template += f"{prompts.SPECIALIZED_TEMPLATE_2['VALIDITY_DATE']}"
    if "VISA_TYPE" in prompts.RECOMMENDED_DOCUMENTS_LISTS_2[doc_type]:
        template += f"{prompts.SPECIALIZED_TEMPLATE_2['VISA_TYPE']}"
    if "SHIP/PROJECT_DEPARTMENT_LEVEL" in prompts.RECOMMENDED_DOCUMENTS_LISTS[doc_type]:
        template += f"{prompts.SPECIALIZED_TEMPLATE_2['SHIP_PROJECT_DEPARTMENT_LEVEL']}"
    if template_corrections:
        template += (
            f"{prompts.TEMPLATE_CORRECTIONS}"
            f"{template_corrections}"
        )
    return template