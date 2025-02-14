SYSTEM_TEMPLATE = ''' 
You are an AI specializing in document classification. Categorize the information based on the following rules: 
''' 
HARDENING_TEMPLATE = ''' 
- Return Output in Valid JSON Format. 
- Exclude the word "json" in output. 
- Determine the Dates based on context. 
- Use YYYY-MM-DD for dates. 
- Correct spelling based on context. 
- If a Category is Not Found, return "Not specified" 
''' 
SPECIALIZED_TEMPLATE = { 
'NAME': ''' 
- Extract the name listed after NAME:. 
- Get nearest relevant name not any other name or title that appears near the beginning of the document.
- DON'T assume the second word is middle name. 
- If three words, first two belong as FIRST_NAME based on common name. 
- Separate the name to LAST_NAME, FIRST_NAME, MIDDLE_NAME
''',
'VALIDITY_DATE':''' 
- Date of Expiry" → VALIDITY_DATE
''' 

} 
RECOMMENDED_DOCUMENTS_LISTS = {
    'flag endorsement':
        '''ISSUING_BODY, POSITION_CERTIFICATE, VALIDITY_DATE, ISSUED_DATE, DOCUMENT_NUMBER''',
    'cop/coc':
        '''ISSUING_BODY, POSITION_CERTIFICATE, VALIDITY_DATE, ISSUED_DATE, DOCUMENT_NUMBER, SHIP/PROJECT_DEPARTMENT_LEVEL''',
    'national certificate':
        '''ISSUING_BODY, POSITION_CERTIFICATE, VALIDITY_DATE, DOCUMENT_NUMBER, DOCUMENT_TYPE''',
    'flag book':
        '''ISSUING_BODY, VALIDITY_DATE, ISSUING_COUNTRY, PLACE_OF_ISSUE, BOOK_NUMBER, COUNTRY, NAME''',
    'seamans book': 
        '''ISSUING_BODY, VALIDITY_DATE, ISSUED_DATE, PLACE_OF_ISSUE, BOOK_NUMBER, COUNTRY, NAME''',
    'visa': 
        '''ISSUING_BODY, VALIDITY_DATE, ISSUED_DATE, DOCUMENT_NUMBER, PLACE_OF_ISSUE, NAME, VISA_TYPE''',
    'passport': 
        '''VALIDITY_DATE, ISSUED_DATE, DOCUMENT_NUMBER, PLACE_OF_ISSUE, COUNTRY, NAME'''
}
