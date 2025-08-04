import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

AMADEUS_CONFIG = {
    'OFFICE_ID': 'KIN1S2312',
    'USERNAME': 'WSCPJCAR',
    'PASSWORD': '6WbmmXZJGS?D',
    'ENDPOINTS': {
        'FLIGHT_AVAILABILITY': 'https://nodeD1.test.webservices.amadeus.com/1ASIWCARCPJ'
    },
}
