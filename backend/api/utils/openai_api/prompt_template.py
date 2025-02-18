SYSTEM_TEMPLATE = """ 
You are a professional AI specializing in clasifying and categorizing [*doc_type*] documents. Classify and categorize carefully the information based on the following rules: 
"""
HARDENING_TEMPLATE = """ 
- Return Output in Valid JSON Format. 
- Exclude the word "json" in output. 
- Determine the Dates based on context. 
- Use YYYY-MM-DD for dates. 
- Correct spelling based on context. 
- If a Category is Not Found, return "Not specified" 
"""
# - DON'T assume the second word is middle name.
# - Here are some First name examples: Harold Paul, Ely
# - If three words, first two belong as FIRST_NAME based on common name.
SPECIALIZED_TEMPLATE = {
    "NAME": """ 
- Extract the name listed after NAME:
- Get nearest relevant name not any other name or title that appears near the beginning of the document.
- Analyze each word before classifying it a first name or Middle name, Mispelled words or cut off words based on context are not viable for first names
- If three words, first two belong as FIRST_NAME based on common name.
- Separate the name to LAST_NAME, FIRST_NAME, MIDDLE_NAME
""",
    "VALIDITY_DATE": """ 
- Date of Expiry → VALIDITY_DATE
""",
    "VISA_TYPE": """ 
- Extract the visa type, typically a single letter or short code (e.g., "G", "B1/B2").
""",
    "SHIP_PROJECT_DEPARTMENT_LEVEL": """  
- Extract the department or division overseeing the ship or project.   
- Prioritize the most specific level if multiple exist.   
""",
}
RECOMMENDED_DOCUMENTS_LISTS = {
    "flag endorsement": """ISSUING_BODY, \nPOSITION_CERTIFICATE, \nVALIDITY_DATE, \nISSUED_DATE, \nDOCUMENT_NUMBER""",
    "cop/coc": """ISSUING_BODY, \nPOSITION_CERTIFICATE, \nVALIDITY_DATE, \nISSUED_DATE, \nDOCUMENT_NUMBER, \nSHIP/PROJECT_DEPARTMENT_LEVEL""",
    "national certificate": """ISSUING_BODY, \nPOSITION_CERTIFICATE, \nVALIDITY_DATE, \nDOCUMENT_NUMBER, \nDOCUMENT_TYPE""",
    "flag book": """ISSUING_BODY, \nVALIDITY_DATE, \nISSUING_COUNTRY, \nPLACE_OF_ISSUE, \nBOOK_NUMBER, \nCOUNTRY, \nNAME""",
    "seamans book": """ISSUING_BODY, \nVALIDITY_DATE, \nISSUED_DATE, \nPLACE_OF_ISSUE, \nBOOK_NUMBER, \nCOUNTRY, \nNAME""",
    "visa": """ISSUING_BODY, \nVALIDITY_DATE, \nISSUED_DATE, \nDOCUMENT_NUMBER, \nVISA_TYPE, \nPLACE_OF_ISSUE, \nNAME""",
    "passport": """VALIDITY_DATE, \nISSUED_DATE, \nDOCUMENT_NUMBER, \nPLACE_OF_ISSUE, \nCOUNTRY, \nNAME""",
}

SYSTEM_TEMPLATE_2 = """ 
You are a professional agent that specializes in clasifying [*doc_type*] documents. Your task is to clasify [*required_docs*] in the given text correctly and accurately.
"""
HARDENING_TEMPLATE_2 = """
Please consider the Dates base on its context.
Please use this format when classifying Dates: YYYY-MM-DD.
Always clasify the [*doc_type*] documents in a valid json format and avoid returning the word json.
Return "Not specified" if no category is found.
"""
SPECIALIZED_TEMPLATE_2 = {
    "NAME": """ 
Always separate the name to LAST_NAME, FIRST_NAME and MIDDLE_NAME.
Please only extract the name after NAME:
Always get the nearest relevant name and not any other name or title that appears near the beginning of the document.
If the first name has three words or more, the first two or three belong as the FIRST_NAME based on common name. An example of this is: JOHN PAUL, MARIA ANN ROSE.
Avoid assumming the second word is middle name.
Words like Sven, Transh is not a valid name, Always check the for naming conventions.

Please always follow this template for name.
NAME: {
LAST_NAME: DELA CRUZ,
FIRST_NAME: JUAN CARLO,
MIDDLE_NAME: LOPEZ
}
""",
    "VALIDITY_DATE": """ 
Please consider that the Date of Expiry is also the VALIDITY_DATE
""",
    "VISA_TYPE": """ 
Always extract the visa type, typically a single letter or a short code (e.g., "G", "B1/B2")
""",
    "SHIP_PROJECT_DEPARTMENT_LEVEL": """  
Always extract the department or division overseeing the ship or project.
Please prioritize the most specific level if multiple exist.  
""",
}

RECOMMENDED_DOCUMENTS_LISTS_2 = {
    "flag endorsement": """ISSUING_BODY, POSITION_CERTIFICATE, VALIDITY_DATE, ISSUED_DATE, DOCUMENT_NUMBER""",
    "cop/coc": """ISSUING_BODY, POSITION_CERTIFICATE, VALIDITY_DATE, ISSUED_DATE, DOCUMENT_NUMBER, SHIP/PROJECT_DEPARTMENT_LEVEL""",
    "national certificate": """ISSUING_BODY, POSITION_CERTIFICATE, VALIDITY_DATE, DOCUMENT_NUMBER, DOCUMENT_TYPE""",
    "flag book": """ISSUING_BODY, VALIDITY_DATE, ISSUING_COUNTRY, PLACE_OF_ISSUE, BOOK_NUMBER, COUNTRY, NAME""",
    "seamans book": """ISSUING_BODY, VALIDITY_DATE, ISSUED_DATE, PLACE_OF_ISSUE, BOOK_NUMBER, COUNTRY, NAME""",
    "visa": """ISSUING_BODY, VALIDITY_DATE, ISSUED_DATE, DOCUMENT_NUMBER, VISA_TYPE, PLACE_OF_ISSUE, NAME""",
    "passport": """VALIDITY_DATE, ISSUED_DATE, DOCUMENT_NUMBER, PLACE_OF_ISSUE, COUNTRY, NAME""",
}
