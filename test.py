from zeep import Client
from zeep.exceptions import Fault
from zeep.plugins import HistoryPlugin
from lxml import etree

import settings
from core.enterprise_core import AmadeusEnterpriseSDK

sdk = AmadeusEnterpriseSDK()

headers_data = sdk.get_headers('availability', 1)
message_id_header = headers_data['message_id']['header']
action_header = headers_data['action']['header']
to_header = headers_data['to']['header']
session_header = headers_data['session']['header']
security_header = headers_data['security']['header']
user_id_header = headers_data['user_id']['header']

history = HistoryPlugin()

client = Client(
    wsdl=settings.AMADEUS_CONFIG['WSDL'],
    plugins=[history]
)

body = {
    'numberOfUnit': {
        'unitNumberDetail': [
            {'numberOfUnits': 2, 'typeOfUnit': 'PX'},
            {'numberOfUnits': 100, 'typeOfUnit': 'RC'}
        ]
    },
    'paxReference': {
        'ptc': 'ADT',
        'traveller': [{'ref': 1}, {'ref': 2}]
    },
    'fareOptions': {
        'pricingTickInfo': {
            'pricingTicketing': {
                'priceType': ['ET', 'RP', 'RU', 'TAC', 'XND', 'XLA', 'XLO', 'XLC', 'XND']
            }
        }
    },
    'travelFlightInfo': {
        'companyIdentity': {
            'carrierQualifier': 'X',
            'carrierId': ['NK', 'F9']
        },
        'flightDetail': {
            'flightType': 'N'
        }
    },
    'itinerary': [
        {
            'requestedSegmentRef': {'segRef': 1},
            'departureLocalization': {'departurePoint': {'locationId': 'HAV'}},
            'arrivalLocalization': {'arrivalPointDetails': {'locationId': 'MAD'}},
            'timeDetails': {'firstDateTimeDetail': {'date': '2025-08-06'}}
        },
        {
            'requestedSegmentRef': {'segRef': 2},
            'departureLocalization': {'departurePoint': {'locationId': 'MAD'}},
            'arrivalLocalization': {'arrivalPointDetails': {'locationId': 'HAV'}},
            'timeDetails': {'firstDateTimeDetail': {'date': '2025-08-13'}}
        }
    ]
}

try:
    response = client.service.Fare_MasterPricerTravelBoardSearch(
        **body,
        _soapheaders=[message_id_header, action_header, to_header, session_header, security_header, user_id_header]
    )
except Fault as e:
    print(f"SOAP Fault: {e}")

if history.last_sent:
    print("Request XML:")
    print(etree.tostring(history.last_sent['envelope'], pretty_print=True).decode())

if history.last_received:
    print("Response XML:")
    print(etree.tostring(history.last_received['envelope'], pretty_print=True).decode())
