SYSTEM_TEMPLATE = '''
You are an AI specializing in document classification. Extract and categorize information based on the following categories:
'''

HARDENING_TEMPLATE = '''
- Output only JSON. No extra text.
- Exclude the word "json" in output.
- Use YYYY-MM-DD for dates.
- Map: "First" → First Name, "Last" → Last Name, "Middle" → Middle Name ,"M.I." → Middle Initial.
- Extract and separate first, middle, and last names.
- If Middle Name or MI is not mentioned, leave it blank.
- Correct spelling based on context.
- If category is not specified, put Not specified.
'''

RECOMMENDED_DOCUMENTS_LISTS = {
    'flag endorsement':
        '''ISSUING_BODY,POSITION_CERTIFICATE,VALIDITY_DATE,ISSUED_DATE,DOCUMENT_NUMBER''',
    'cop/coc':
        '''ISSUING_BODY,POSITION_CERTIFICATE,VALIDITY_DATE,ISSUED_DATE,DOCUMENT_NUMBER,SHIP/PROJECT_DEPARTMENT_LEVEL''',
    'national certificate':
        '''ISSUING_BODY,POSITION_CERTIFICATE,VALIDITY_DATE,DOCUMENT_NUMBER,DOCUMENT_TYPE''',
    'flag book':
        '''ISSUING_BODY,VALIDITY_DATE,ISSUING_COUNTRY,PLACE_OF_ISSUE,BOOK_NUMBER,COUNTRY,LAST_NAME,FIRST_NAME,MIDDLE_NAME,''',
    'seamans book': 
        '''ISSUING_BODY,VALIDITY_DATE,ISSUED_DATE,PLACE_OF_ISSUE,BOOK_NUMBER,COUNTRY,LAST_NAME,FIRST_NAME''',
    'visa': 
        '''ISSUING_BODY,VALIDITY_DATE,ISSUED_DATE,DOCUMENT_NUMBER,PLACE_OF_ISSUE,LAST_NAME,FIRST_NAME,MIDDLE_NAME,VISA_TYPE''',
    'passport': 
        '''VALIDITY_DATE,ISSUED_DATE,DOCUMENT_NUMBER,PLACE_OF_ISSUE,COUNTRY,LAST_NAME,FIRST_NAME,MIDDLE_NAME,'''
}
