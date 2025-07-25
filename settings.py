import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

AMADEUS_CONFIG = {
    'WSDL': os.path.join(BASE_DIR, 'wsdl', '1ASIWPOC1A_PDT_20240516_153443.wsdl'),
    'OFFICE_ID': os.getenv('AMADEUS_OFFICE_ID'),
    'USERNAME': os.getenv('AMADEUS_USERNAME'),
    'PASSWORD': os.getenv('AMADEUS_PASSWORD'),
}

NSMAP = {
    'add': 'http://www.w3.org/2005/08/addressing',
    'awsse': 'http://xml.amadeus.com/2010/06/Session_v3',
    'oas': 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd',
    'oas1': 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd'
}
